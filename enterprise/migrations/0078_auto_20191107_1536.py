# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-07 15:36


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0077_auto_20191002_1529'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enterprisecustomeruser',
            options={'ordering': ['active', '-modified'], 'verbose_name': 'Enterprise Customer Learner', 'verbose_name_plural': 'Enterprise Customer Learners'},
        ),
    ]
