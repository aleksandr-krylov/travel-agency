"""travelagency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from users import views as user_views
from orders.views import (
    checkout,
    payment,
    orders,
    order_done
)
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/news-edit/', user_views.NewsEditListView.as_view(), name='news-edit'),
    path('admin/blog-edit/', user_views.BlogEditListView.as_view(), name='blog-edit'),
    path('admin/catalog-list/', user_views.catalog_list, name='catalog-list'),
    path('admin/bustours-edit/', user_views.BusTourEditListView.as_view(), name='bustours-edit'),
    path('admin/cruises-edit/', user_views.CruiseEditListView.as_view(), name='cruises-edit'),
    path('admin/managers-edit/', user_views.managers_list, name='managers-edit'),
    path('admin/news-post/<int:pk>/delete/', user_views.NewsPostDeleteView.as_view(), name='news-post-delete'),
    path('admin/blog-post/<int:pk>/delete/', user_views.BlogPostDeleteView.as_view(), name='blog-post-delete'),
    path('admin/bus-tour/<int:pk>/delete/', user_views.BusTourDeleteView.as_view(), name='bus-tour-delete'),
    path('admin/cruise/<int:pk>/delete/', user_views.CruiseDeleteView.as_view(), name='cruise-delete'),
    path('admin/manager/<int:pk>/delete/', user_views.manager_confirm_delete, name='manager-delete'),
    path('admin/news-post/create', user_views.newspost_create, name='news-post-create'),
    path('admin/blog-post/create', user_views.blogpost_create, name='blog-post-create'),
    path('admin/bus-tour/create', user_views.bustour_create, name='bus-tour-create'),
    path('admin/cruise/create', user_views.cruise_create, name='cruise-create'),
    path('admin/manager/create', user_views.manager_create, name='manager-create'),
    path('orders-edit/', orders, name='orders-edit'),
    path('order/<int:pk>/done', order_done, name='order-done'),
    path('', include('mainapp.urls')),
    path('blog/', include('blog.urls')),
    path('catalog/', include('catalog.urls')),
    path('cart/', include('carts.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('accounts/profile/', user_views.profile, name='profile'),
    path('checkout/', checkout, name='checkout'),
    path('payment/', payment, name='payment'),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()

