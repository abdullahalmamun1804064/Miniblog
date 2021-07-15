from django.contrib import admin
from .models import post

@admin.register(post)
class post_model_admin(admin.ModelAdmin):
    list_display=['id','title','disc']
