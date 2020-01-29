from django.db import models
from django.contrib.auth.models import User
# from embed_video.fields import EmbedVideoField

# Create your models here.
# class VideoList(models.Model):
#     video = EmbedVideoField()

class Videos(models.Model):
    title = models.CharField(max_length=200)
    videofile = models.FileField(upload_to='videos',verbose_name="")
    desc = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    active_flag = models.BooleanField(default=True)


class CurrentProject(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title

class CurrentProjectImages(models.Model):
    title = models.ForeignKey(CurrentProject,default=None, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='currentProjectImages', verbose_name = "")


class News(models.Model):
    title = models.CharField(max_length = 200)
    body = models.CharField(max_length=2000)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Reviews(models.Model):
    full_name = models.CharField(max_length=100)
    organisation = models.CharField(max_length=100, blank=True, null=True)
    body = models.CharField(max_length=500)
    active_flag = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.body