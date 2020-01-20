from django.db import models
from django.contrib.auth.models import User


category_list = (
    ('general', 'GENERAL'),
    ('support', 'SUPPORT'),
    ('bugReport', 'BUG REPORT'),
)
# Create your models here.
class CommunicationEmails(models.Model):
    category = models.CharField(max_length=20,choices=category_list,default='general')
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True,blank=True)
    from_email = models.EmailField()
    #full_name = models.CharField(max_length=100,null=True,blank=True)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.subject
