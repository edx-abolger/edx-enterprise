# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-13 17:08


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0079_AddEnterpriseEnrollmentSource'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enterprisecustomeruser',
            options={'ordering': ['-active', '-modified'], 'verbose_name': 'Enterprise Customer Learner', 'verbose_name_plural': 'Enterprise Customer Learners'},
        ),
    ]
