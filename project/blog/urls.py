from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('english/', views.english, name='blog-english'),
    path('math/', views.math, name='blog-math'),
    path('science/', views.science, name='blog-science'),
    path('login/', views.login, name='blog-login'),
    path('register/', views.register, name='blog-register'),
    path('about/', views.about, name='blog-about'),
]
