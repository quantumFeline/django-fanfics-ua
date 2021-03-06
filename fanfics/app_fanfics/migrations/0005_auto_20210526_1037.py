# Generated by Django 2.1.15 on 2021-05-26 07:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_fanfics', '0004_auto_20210526_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='publication_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Published:'),
        ),
        migrations.AlterField(
            model_name='fanfic',
            name='publication_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Published:'),
        ),
    ]
