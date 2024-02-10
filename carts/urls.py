from django.urls import path
from . import views


urlpatterns = [
    path('bus-tour/<int:pk>/add-to-cart', views.bustour_add_to_cart, name='bustour-add-to-cart'),
    path('bus-tour/<int:pk>/remove-from-cart', views.bustour_remove_from_cart, name='bustour-remove-from-cart'),
    path('cruise/<int:pk>/add-to-cart', views.cruise_add_to_cart, name='cruise-add-to-cart'),
    path('cruise/<int:pk>/remove-from-cart', views.cruise_remove_from_cart, name='cruise-remove-from-cart'),
    path('', views.cart, name='cart')
]