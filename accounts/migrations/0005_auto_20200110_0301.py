# Generated by Django 3.0.1 on 2020-01-09 21:31

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200110_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
