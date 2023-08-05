# Generated by Django 4.2 on 2023-08-01 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=55)),
                ('username', models.CharField(max_length=30)),
                ('password1', models.CharField(max_length=35)),
                ('password2', models.CharField(max_length=35)),
            ],
        ),
        migrations.AlterField(
            model_name='slider',
            name='firstbuttontitle',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='slider',
            name='secoundbuttontitle',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='slider',
            name='titlebottom',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='slider',
            name='titleheader',
            field=models.CharField(max_length=50),
        ),
    ]