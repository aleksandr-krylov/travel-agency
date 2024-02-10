from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Post, Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


class CommentAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)