from django.contrib import admin
from .models import Videos
# Register your models here.

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('title','created_date')


