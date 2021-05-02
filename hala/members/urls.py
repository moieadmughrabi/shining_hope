from django.contrib import admin
from django.urls import path

from .views  import *
from .import views 
urlpatterns = [
    
   
    path('register/',UserRgestrationview.as_view() ,name='register'),
    
]

