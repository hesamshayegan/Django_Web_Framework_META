from django.urls import path
from . import views

urlpatterns = [
    path('menu-items-drf', views.MenuItemsView.as_view()),
    path('menu-items-drf/<int:pk>', views.SingleMenuItemView.as_view()),
]