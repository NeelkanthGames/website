from django.contrib import admin
from .models import Videos, CurrentProjectImages, CurrentProject, News, Reviews
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

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','body','created_date')

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('full_name','organisation','body','created_date')
