# Generated by Django 3.0 on 2021-03-29 07:56

import django.core.files.storage
from django.db import migrations
import rw.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rw', '0038_auto_20210329_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='file',
            field=rw.fields.ValidatedFileField(blank=True, help_text='Upload file', null=True, storage=django.core.files.storage.FileSystemStorage(base_url='/rwmedia/', location='/var/www/roundware/rwmedia/'), upload_to='.'),
        ),
    ]
