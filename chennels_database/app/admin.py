from django.contrib import admin
from .models import*


@admin.register(Chat)
class Chatadmin(admin.ModelAdmin):
    list_display=['id','content','group','timestamp']
    
    
@admin.register(Group)
class Chatadmin(admin.ModelAdmin):
    list_display=['id','name']
