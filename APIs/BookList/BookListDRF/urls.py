from django.urls import path
from . import views

urlpatterns = [
    path('books-drf', views.BookView.as_view()),
    path('books-drf/<int:pk>', views.SingleBookView.as_view()),
]
