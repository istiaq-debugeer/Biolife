# Generated by Django 4.2.1 on 2023-09-16 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
    ]
