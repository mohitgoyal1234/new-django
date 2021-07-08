from django.urls import path,include
from . import views

urlpatterns =[
    path('blog/', views.Blog, name='blog'),
    path('latestblog/', include('latestblog.urls')),
    path('previousblog/', include('previousblog.urls')),
]
