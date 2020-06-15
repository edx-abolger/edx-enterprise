# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-24 15:45


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sap_success_factors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsapsuccessfactorsenterprisecustomerconfiguration',
            name='sapsf_company_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='SAP Company ID'),
        ),
        migrations.AddField(
            model_name='historicalsapsuccessfactorsenterprisecustomerconfiguration',
            name='sapsf_user_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='SAP User ID'),
        ),
        migrations.AddField(
            model_name='sapsuccessfactorsenterprisecustomerconfiguration',
            name='sapsf_company_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='SAP Company ID'),
        ),
        migrations.AddField(
            model_name='sapsuccessfactorsenterprisecustomerconfiguration',
            name='sapsf_user_id',
            field=models.CharField(blank=True, max_length=255, verbose_name='SAP User ID'),
        ),
        migrations.AlterField(
            model_name='historicalsapsuccessfactorsenterprisecustomerconfiguration',
            name='sapsf_base_url',
            field=models.CharField(max_length=255, verbose_name='SAP Base URL'),
        ),
        migrations.AlterField(
            model_name='sapsuccessfactorsenterprisecustomerconfiguration',
            name='sapsf_base_url',
            field=models.CharField(max_length=255, verbose_name='SAP Base URL'),
        ),
    ]
