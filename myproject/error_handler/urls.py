from django.urls import path
from . import views 


urlpatterns = [ 
    path('error/', views.my_error_handler, name='my_error_handler'),
]