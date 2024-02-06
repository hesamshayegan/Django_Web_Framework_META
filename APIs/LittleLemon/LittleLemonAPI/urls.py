from django.urls import path
from . import views

urlpatterns = [
    path('menu-items', views.menu_items),
    path('menu-items/<int:pk>', views.menu_items),
    path('menu',views.menu),
    path('welcome',views.welcome),
]
