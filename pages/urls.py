from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index_landing_page, name = 'landing_page'),
    path('home/', views.homepage, name = 'home'),
    path('upload_videos/', views.upload_videos, name = 'upload_videos'),
    path('upload_current_project/', views.upload_current_project, name = 'upload_current_project'),
    path('upload_news/',views.upload_news, name = 'upload_news'),
    path('upload_reviews/',views.upload_reviews, name = 'upload_reviews'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
