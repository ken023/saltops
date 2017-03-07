# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy_manager', '0005_auto_20170120_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='host',
            field=models.ManyToManyField(blank=True, default='', through='deploy_manager.ProjectHost', to='cmdb.Host', verbose_name='\u4e3b\u673a'),
        ),
    ]