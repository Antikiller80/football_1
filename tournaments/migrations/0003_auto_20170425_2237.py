# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_auto_20170420_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='club_images/', verbose_name='Логотип клуба'),
        ),
        migrations.AlterField(
            model_name='player',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='players_images/', verbose_name='Фото игрока'),
        ),
    ]
