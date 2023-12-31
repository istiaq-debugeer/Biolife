# Generated by Django 4.2.1 on 2023-09-16 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bannerimage', models.ImageField(upload_to='banner/')),
                ('firstline', models.CharField(max_length=50)),
                ('secoundline', models.CharField(max_length=50)),
                ('thirdline', models.CharField(max_length=50)),
                ('fourthline', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='bannerMovinImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movingimage', models.ImageField(upload_to='moveimage/')),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogImage', models.ImageField(upload_to='blog/')),
                ('blogheader', models.CharField(max_length=50)),
                ('blogeradminImage', models.ImageField(upload_to='blog/admin/')),
                ('postdate', models.DateTimeField(auto_now=True)),
                ('blogditails', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carousel', models.ImageField(upload_to='carousel/')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('subcattegorry', models.CharField(blank=True, max_length=50)),
                ('icon', models.CharField(blank=True, max_length=20)),
                ('subcategory', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textcomment', models.TextField(max_length=500)),
                ('publishdate', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task1.blogpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('message', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FolloUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instaImage', models.ImageField(upload_to='insta/')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.BooleanField(default=False, null=True)),
                ('productimage', models.ImageField(upload_to='toprelatedProduct/')),
                ('productcategory', models.CharField(max_length=50)),
                ('productname', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=90)),
                ('oldprice', models.DecimalField(decimal_places=2, max_digits=90)),
                ('productDiscription', models.TextField(max_length=200)),
                ('category', models.ManyToManyField(to='task1.category')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slideImage', models.ImageField(upload_to='slider/')),
                ('slidetitle', models.CharField(max_length=50)),
                ('titleheader', models.CharField(max_length=50)),
                ('titlebottom', models.CharField(max_length=50)),
                ('firstbuttontitle', models.CharField(max_length=50)),
                ('secoundbuttontitle', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productimage', models.ImageField(upload_to='SpecialOffer/')),
                ('text1', models.CharField(max_length=30)),
                ('text2', models.CharField(max_length=30)),
                ('text3', models.CharField(max_length=30)),
                ('text4', models.CharField(max_length=30)),
                ('boldtext', models.CharField(max_length=30)),
                ('productname', models.CharField(max_length=50)),
                ('productprice', models.DecimalField(decimal_places=2, default=0, max_digits=100)),
                ('productamount', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WebsiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='logo/')),
                ('email', models.CharField(max_length=40)),
                ('twitterlink', models.CharField(max_length=100)),
                ('facebooklink', models.CharField(max_length=100)),
                ('youtubelink', models.CharField(max_length=100)),
                ('instagramlink', models.CharField(max_length=100)),
                ('linkdeinlink', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=50)),
                ('availableTime', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SecondSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slideheader', models.CharField(max_length=40)),
                ('firsttitle', models.CharField(max_length=70)),
                ('secoundtitle', models.CharField(max_length=80)),
                ('productname', models.CharField(max_length=80)),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task1.products')),
            ],
        ),
        migrations.CreateModel(
            name='DealsOfTheDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('targetdatetime', models.DateTimeField()),
                ('productcategory', models.CharField(max_length=50)),
                ('productname', models.CharField(max_length=50)),
                ('productditails', models.CharField(max_length=50)),
                ('button', models.CharField(max_length=40)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task1.products')),
            ],
        ),
        migrations.CreateModel(
            name='CommentAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(upload_to='attachment/')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task1.comment')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task1.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task1.products')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(through='task1.CartItem', to='task1.products'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(to='task1.tag'),
        ),
    ]
