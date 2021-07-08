from django.urls import path
from . import views

urlpatterns =[
    path('events/', views.Events, name='events'),
]
