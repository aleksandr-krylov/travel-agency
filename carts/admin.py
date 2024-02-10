from django.contrib import admin
from .models import BusTourCartItem, CruiseCartItem, Cart
# Register your models here.

admin.site.register(BusTourCartItem)
admin.site.register(CruiseCartItem)
admin.site.register(Cart)