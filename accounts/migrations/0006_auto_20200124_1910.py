# Generated by Django 3.0.1 on 2020-01-24 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200110_0301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='is_staff',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='user_type',
            field=models.CharField(choices=[('user', 'user'), ('staff', 'staff'), ('admin', 'admin')], default='user', max_length=20),
        ),
    ]
