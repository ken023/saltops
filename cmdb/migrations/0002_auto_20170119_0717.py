# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 07:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='Services_Code',
        ),
        migrations.RemoveField(
            model_name='host',
            name='cpu',
        ),
        migrations.RemoveField(
            model_name='host',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='host',
            name='editor',
        ),
        migrations.RemoveField(
            model_name='host',
            name='eth1',
        ),
        migrations.RemoveField(
            model_name='host',
            name='eth2',
        ),
        migrations.RemoveField(
            model_name='host',
            name='guarantee_date',
        ),
        migrations.RemoveField(
            model_name='host',
            name='hard_disk',
        ),
        migrations.RemoveField(
            model_name='host',
            name='internal_ip',
        ),
        migrations.RemoveField(
            model_name='host',
            name='mac',
        ),
        migrations.RemoveField(
            model_name='host',
            name='memory',
        ),
        migrations.RemoveField(
            model_name='host',
            name='number',
        ),
        migrations.RemoveField(
            model_name='host',
            name='server_sn',
        ),
        migrations.RemoveField(
            model_name='host',
            name='switch_port',
        ),
        migrations.RemoveField(
            model_name='host',
            name='vm',
        ),
    ]