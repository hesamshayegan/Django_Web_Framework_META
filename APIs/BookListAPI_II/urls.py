from django.urls import path, include 
from . import views
urlpatterns = [
    # path('books/', views.books)
    path('books', views.BookList.as_view()),
    path('books/<int:pk>', views.Book.as_view()),
    path('__debug__/', include('debug_toolbar.urls'))
]