from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog-post/<int:pk>/', views.blogpost, name='blog-post'),
]