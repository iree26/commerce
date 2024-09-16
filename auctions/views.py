from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import ListingForm
from .models import User, Listing, Watchlist, Bid, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def index(request):
    listings = Listing.objects.all()
    
    return render(request, "auctions/index.html",{
        "listings":listings
    })

def create_list(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index") 
    else:
        form = ListingForm()
    return render(request, 'auctions/create_list.html', {
        "form": form
        })

def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    
def listing_page(request, listing_id):
    
    listing = get_object_or_404(Listing, id=listing_id)
    
    
    return render(request, "auctions/listing.html", {
        "listing": listing
    })
    
@login_required
def add_to_watchlist(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)

    
    if request.user in listing.watchlist.all():
        listing.watchlist.remove(request.user)  
    else:
        listing.watchlist.add(request.user)  

    return redirect(reverse('listing_page', args=[listing_id]))

@login_required
def place_bid(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    current_bids = listing.bids.all()
    bid_amount = None  

    if request.method == "POST":
        bid_amount_str = request.POST.get("bid")
        
        if bid_amount_str:
            try:
                bid_amount = float(bid_amount_str)
            except ValueError:
                return render(request, "auctions/listing.html", {
                    "listing": listing,
                    "message": "Please enter a valid bid amount."
                })
            
            highest_bid = max([bid.amount for bid in current_bids], default=listing.starting_bid)

            if bid_amount > highest_bid:
                new_bid = Bid(listing=listing, user=request.user, amount=bid_amount)
                new_bid.save()
                return HttpResponseRedirect(reverse("listing_page", args=[listing.id]))
            else:
                return render(request, "auctions/listing.html", {
                    "listing": listing,
                    "message": "Your bid must be higher than the current highest bid."
                })

    return render(request, "auctions/listing.html", {
        "listing": listing,
        
    })

    
    
@login_required
def close_auction(request, id):
    listing = get_object_or_404(Listing, id=id)
    
    
    if request.user == listing.user:
        listing.is_active = False
        listing.save()
        messages.success(request, "The auction has been closed.")
    else:
        messages.error(request, "You are not authorized to close this auction.")
    
    return HttpResponseRedirect(reverse('listing_page', args=[id]))

@login_required
def add_comment(request, id):
    listing = get_object_or_404(Listing, id=id)
    if request.method == "POST":
        comment = Comment(user=request.user, listing=listing, content=request.POST.get("comment"))
        comment.save()
    return HttpResponseRedirect(reverse('listing_page', args=[id]))

@login_required
def watchlist(request):
    user_watchlist = request.user.watchlist_listings.all()  
    return render(request, "auctions/my_watchlist.html", {
        "watchlist": user_watchlist
    })


def categories(request):
    categories = Listing.objects.values_list('category', flat=True).distinct()
    return render(request, "auctions/categories.html", {
        "categories": categories
    })


def category_listings(request, category):
    listings = Listing.objects.filter(category=category, is_active=True)
    return render(request, "auctions/category_listings.html", {
        "category": category,
        "listings": listings
    })