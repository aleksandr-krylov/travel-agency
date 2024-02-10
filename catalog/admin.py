from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from .models import BusTour, Cruise, TourDate, Service, Ferry, Cabin

# Register your models here.
class BusTourAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

class CruiseAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

class CabinAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(BusTour, BusTourAdmin)
admin.site.register(Cruise, CruiseAdmin)
admin.site.register(TourDate)
admin.site.register(Service)
admin.site.register(Ferry)
admin.site.register(Cabin, CabinAdmin)