from django.urls import path
from . import views

urlpatterns =[
    path('faqs/', views.Faqs, name='faqs'),
]
