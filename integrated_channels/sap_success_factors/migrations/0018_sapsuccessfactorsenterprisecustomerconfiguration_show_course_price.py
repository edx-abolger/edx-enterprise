# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-02 13:09


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sap_success_factors', '0017_sapsuccessfactorsglobalconfiguration_search_student_api_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='sapsuccessfactorsenterprisecustomerconfiguration',
            name='show_course_price',
            field=models.BooleanField(default=False),
        ),
    ]
