#for Flights

from django.urls import path
from .  views import *

urlpatterns=[
    path('',login_view,name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/",register , name="register"),
    path("home/",home,name="home"),
    path("Airport/",details,name="details"),
    path("flight/",flight,name="flight"),
    path("flight/<int:flight_id>/",flight_no,name="flight_no"),
    path("flight/<int:flight_id>/book/",book,name="book"),
    path("Airport/<int:airport_id>/",airport_no,name="airport_no"),
    path("passenger_book/",passenger_book,name="passenger_book"),
    path("<int:id>/delete",delete,name="delete")
    ]


