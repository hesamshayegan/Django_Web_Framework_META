from django.urls import path
from . import views 

urlpatterns = [
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
    path('', views.home, name="home"),
    path('aboutus/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('home/', views.form_view),
    path('booking/', views.booking_form_view),
    path('hello/', views.index),
    path('menuitem/', views.menuitem),
    path('menu/', views.menu),
]

