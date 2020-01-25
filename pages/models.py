from django.db import models
# from embed_video.fields import EmbedVideoField

# Create your models here.
# class VideoList(models.Model):
#     video = EmbedVideoField()

class Videos(models.Model):
    title = models.CharField(max_length=200)
    videofile = models.FileField(upload_to='videos/',verbose_name="")
    desc = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    active_flag = models.BooleanField(default=True)
