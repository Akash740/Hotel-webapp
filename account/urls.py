from django.urls import path
from . import views



urlpatterns=[
    path('reg/',views.reg,name='reg'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('book_room/',views.book, name="book_room"),
    path('booking_details/',views.booking_details,name="booking_details"),




]