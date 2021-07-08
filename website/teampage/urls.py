from django.urls import path
from . import views

urlpatterns =[
    path('teams/', views.Team, name='team'),
]
