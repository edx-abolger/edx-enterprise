# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-09 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0044_reporting_config_multiple_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprisecustomerreportingconfiguration',
            name='report_type',
            field=models.CharField(choices=[('csv', 'csv'), ('json', 'json')], default='csv', help_text='The type this report should be sent as, e.g. CSV.', max_length=20, verbose_name='Report Type'),
        ),
    ]