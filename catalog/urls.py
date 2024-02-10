from django.urls import path
from . import views


urlpatterns = [
    #path('', views.catalog, name='catalog'),
    path('bus-tours/est/', views.bustours_est, name='bustours-est'),
    path('bus-tours/lv/', views.bustours_lv, name='bustours-lv'),
    path('bus-tours/lt/', views.bustours_lt, name='bustours-lt'),
    path('bus-tours/ru/', views.bustours_ru, name='bustours-ru'),
    path('cruises/', views.cruises, name='cruises'),
    path('bus-tour/<int:pk>/', views.bustour_page, name='bustour-page'),
    path('cruise/<int:pk>/', views.cruise_page, name='cruise-page'),
    path('bus-tour/<int:pk>/book', views.bustour_book, name='bustour-book'),
    path('cruise/<int:pk>/book', views.cruise_book, name='cruise-book'),
]
