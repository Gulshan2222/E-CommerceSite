
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("basic/",views.basic, name="Basic"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Searching"),
    path("products/<int:myid>", views.pview, name="ProductViewing"),
    path("checkout/", views.checkout, name="CheckOut"),
]