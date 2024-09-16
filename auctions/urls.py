from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_list, name="create_list"),
    path("listings/<int:listing_id>/", views.listing_page, name="listing_page"),
    path('add_to_watchlist/<int:listing_id>', views.add_to_watchlist, name='add_to_watchlist'),
    path('place_bid/<int:listing_id>', views.place_bid, name="place_bid" ),
     path("listing/<int:id>/close", views.close_auction, name="close_auction"),
    path("listing/<int:id>/comment", views.add_comment, name="add_comment"),
    path("watchlist/", views.watchlist, name="my_watchlist"),
    path("categories/", views.categories, name="categories"),
    path("categories/<str:category>/", views.category_listings, name="category_listings")

]  