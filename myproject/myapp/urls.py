from django.urls import path
from . import views 

urlpatterns = [
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
    path('', views.home, name="home"),
    path('aboutus/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('book/', views.book, name="book"),
]

