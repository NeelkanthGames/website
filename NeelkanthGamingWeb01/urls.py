from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('', include('accounts.urls')),
    path('games/', include('games.urls')),
    path('videos/', include('videos.urls')),
    path('jobs/', include('jobs.urls')),
    path('contactUs',include('communications.urls'))
]
