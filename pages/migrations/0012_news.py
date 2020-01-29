# Generated by Django 3.0.1 on 2020-01-29 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20200128_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=2000)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
