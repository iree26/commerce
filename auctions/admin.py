from django.contrib import admin
from .models import Listing, Watchlist, Bid, Comment

# Register your models here.

admin.site.register(Listing)
admin.site.register(Watchlist)
admin.site.register(Bid)
admin.site.register(Comment)