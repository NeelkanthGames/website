from django.contrib import admin
from .models import Videos, CurrentProjectImages, CurrentProject
# Register your models here.

@admin.register(Videos)
class VideosAdmin(admin.ModelAdmin):
    list_display = ('title','created_date')

@admin.register(CurrentProject)
class CurrentProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')


@admin.register(CurrentProjectImages)
class CurrentProjectImagesAdmin(admin.ModelAdmin):
    list_display = ('title',)

