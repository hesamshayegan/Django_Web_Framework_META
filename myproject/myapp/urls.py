from django.urls import path
from . import views 

urlpatterns = [
    # path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
    # path('booking/', views.booking_form_view),
    # path('hello/', views.index),
    # path('menuitem/', views.menuitem),
    path('home/', views.Home, name="home"),
    path('about/', views.About, name="about"),
    path('menu/', views.Menu, name="menu"),
    path('book/', views.Book, name="book"),
]

