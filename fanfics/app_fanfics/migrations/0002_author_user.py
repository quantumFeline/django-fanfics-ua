# Generated by Django 2.1.15 on 2021-05-24 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_fanfics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
