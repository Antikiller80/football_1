# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 10:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='post.Category', verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='article',
            name='championship',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='championship', to='tournaments.Championship', verbose_name='Чемпионат'),
        ),
        migrations.AlterField(
            model_name='article',
            name='match',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='match', to='tournaments.Matches', verbose_name='Матч'),
        ),
    ]
