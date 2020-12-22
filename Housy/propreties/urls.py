from django.urls import path
from . import views

urlpatterns = [

    path('', views.propreties , name='propreties'),
    
    
]