from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),
    path('news/news-post/<int:pk>/', views.newspost, name='news-post'),
    path('services/', views.services, name='services'),
    path('contact-us/', views.contacts, name='contact-us'),
    
    
]