# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-24 11:41


import jsonfield.fields

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0069_auto_20190613_0607'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnterpriseCatalogQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(default='All Content', max_length=255)),
                ('content_filter', jsonfield.fields.JSONField(blank=True, default={}, help_text="Query parameters which will be used to filter the discovery service's search/all endpoint results, specified as a JSON object. An empty JSON object means that all available content items will be included in the catalog.", null=True)),
            ],
            options={
                'ordering': ['created'],
                'verbose_name': 'Enterprise Catalog Query',
                'verbose_name_plural': 'Enterprise Catalog Queries',
            },
        ),
        migrations.AddField(
            model_name='enterprisecustomercatalog',
            name='enterprise_catalog_query',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='enterprise_customer_catalogs', to='enterprise.EnterpriseCatalogQuery'),
        ),
        migrations.AddField(
            model_name='historicalenterprisecustomercatalog',
            name='enterprise_catalog_query',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='enterprise.EnterpriseCatalogQuery'),
        ),
    ]
