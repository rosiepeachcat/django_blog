# Generated by Django 3.2.6 on 2021-08-20 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_post_excerpt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='excerpt',
        ),
        migrations.AddField(
            model_name='post',
            name='quote',
            field=models.TextField(default='Enter Quote', max_length=300),
        ),
    ]
