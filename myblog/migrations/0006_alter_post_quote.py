# Generated by Django 3.2.6 on 2021-08-22 14:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_auto_20210820_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='quote',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
