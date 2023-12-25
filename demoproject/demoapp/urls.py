from django.urls import path
from . import views 


urlpatterns = [ 
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),
    path('say_hello/', views.say_hello, name='say_hello'),
    path('display_date/', views.display_date, name='display_date'),
]