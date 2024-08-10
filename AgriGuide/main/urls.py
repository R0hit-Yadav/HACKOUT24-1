from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('news-updates/', views.news_updates, name='news_updates'),
    path('register/', views.register, name='register'),
     path('logout/', views.custom_logout_view, name='logout'),
]