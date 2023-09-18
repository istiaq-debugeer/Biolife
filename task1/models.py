from django.contrib.auth.models import User
from django.db import models


# Create your models he

class Category(models.Model):
    title = models.CharField(max_length=50, blank=True)
    subcattegorry = models.CharField(max_length=50, blank=True, )
    icon = models.CharField(max_length=20, blank=True)
    subcategory = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @property
    def get_products(self):
        return self.products_set.all()


class Products(models.Model):
    category = models.ManyToManyField(Category)
    subcategory = models.BooleanField(default=False, null=True)
    productimage = models.ImageField(upload_to='toprelatedProduct/')
    productcategory = models.CharField(max_length=50)
    productname = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=90, decimal_places=2)
    oldprice = models.DecimalField(max_digits=90, decimal_places=2)
    productDiscription = models.TextField(max_length=200)

    def __str__(self):
        return self.productname

    def __str__(self):
        return f"product: {self.productname} - {self.id}"
    @property
    def get_deals(self):
        return self.dealsoftheday_set.all()

    @property
    def get_secound_slider(self):
        return self.secondslider_set.all()
class Slider(models.Model):
    slideImage = models.ImageField(upload_to='slider/')
    slidetitle = models.CharField(max_length=50)
    titleheader = models.CharField(max_length=50)
    titlebottom = models.CharField(max_length=50)
    firstbuttontitle = models.CharField(max_length=50)
    secoundbuttontitle = models.CharField(max_length=50)


class SecondSlider(models.Model):
    slider=models.ForeignKey(Products,on_delete=models.CASCADE)
    slideheader = models.CharField(max_length=40)
    firsttitle = models.CharField(max_length=70)
    secoundtitle = models.CharField(max_length=80)
    productname = models.CharField(max_length=80)


    def get_product(self):
        return self.slider.productimage


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class BlogPost(models.Model):
    blogImage = models.ImageField(upload_to='blog/')
    blogheader = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    blogeradminImage = models.ImageField(upload_to='blog/admin/')
    postdate = models.DateTimeField(auto_now=True)
    blogditails = models.TextField(max_length=500)

    # def get_tags(self):
    #     return BlogPost.objects.filter(tags__in=self.tags.all())

    def __str__(self):
        return f"blog: {self.blogheader} - {self.id}"

    @property
    def get_comments(self):
        return self.comment_set.all()

    @property
    def get_count(self):
        return self.comment_set.count()
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    textcomment = models.TextField(max_length=500)
    publishdate = models.DateTimeField(auto_now=True)
    post=models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    @property
    def get_short_comment(self):
        return self.textcomment[:10]


class CommentAttachment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='attachment/')


class DealsOfTheDay(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    targetdatetime = models.DateTimeField()
    productcategory = models.CharField(max_length=50)
    productname = models.CharField(max_length=50)
    productditails = models.CharField(max_length=50)
    button=models.CharField(max_length=40)

    def get_product_image(self):
        return self.product.productimage

    def __str__(self):
        return f"Cart: {self.user} - {self.id}"

    def __str__(self):
        return f"Cart: {self.productname} - {self.id}"


class Banner(models.Model):
    bannerimage = models.ImageField(upload_to='banner/')
    firstline = models.CharField(max_length=50)
    secoundline = models.CharField(max_length=50)
    thirdline = models.CharField(max_length=50)
    fourthline = models.CharField(max_length=50)


class Carousel(models.Model):
    carousel = models.ImageField(upload_to='carousel/')


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class bannerMovinImage(models.Model):
    movingimage = models.ImageField(upload_to='moveimage/')


class FolloUs(models.Model):
    instaImage = models.ImageField(upload_to='insta/')

    def __str__(self):
        self.productname


class SpecialOffer(models.Model):
    productimage = models.ImageField(upload_to='SpecialOffer/')
    text1 = models.CharField(max_length=30)
    text2 = models.CharField(max_length=30)
    text3 = models.CharField(max_length=30)
    text4 = models.CharField(max_length=30)
    boldtext = models.CharField(max_length=30)
    productname = models.CharField(max_length=50)
    productprice = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    productamount = models.CharField(max_length=50)

    def __str__(self):
        return self.productname


class WebsiteSetting(models.Model):
    logo = models.ImageField(upload_to='logo/')
    email = models.CharField(max_length=40)
    twitterlink = models.CharField(max_length=100)
    facebooklink = models.CharField(max_length=100)
    youtubelink = models.CharField(max_length=100)
    instagramlink = models.CharField(max_length=100)
    linkdeinlink = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=50)
    availableTime = models.CharField(max_length=100)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(Products, through='CartItem')

    def __str__(self):
        return f"Cart: {self.user} - {self.id}"

    def clear_cart(self):
        self.items.clear()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.quantity)
