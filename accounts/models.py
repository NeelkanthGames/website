from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    country = CountryField(blank_label='Country')
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_subscribed = models.BooleanField(max_length=1,default=False,null=True)
    is_staff = models.CharField(max_length=1,null=True)
    def __str__(self):
        return self.user.username

