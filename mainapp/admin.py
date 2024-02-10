from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import News

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(News, NewsAdmin)