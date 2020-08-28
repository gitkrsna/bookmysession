from django.urls import path
from .views import *

urlpatterns = [
    path('', demobook),
    path('confirmation', confirmation),
    
]