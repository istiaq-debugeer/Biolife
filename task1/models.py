from django.db import models

# Create your models he

class Slider(models.Model):
    slideImage=models.ImageField(upload_to='slider/')
    slidetitle=models.CharField(max_length=50)
    titleheader=models.CharField(max_length=50)
    titlebottom=models.CharField(max_length=50)
    firstbuttontitle=models.CharField(max_length=50)
    secoundbuttontitle=models.CharField(max_length=50)


class User(models.Model):
        email=models.EmailField(max_length=55)
        username=models.CharField(max_length=30)
        password1=models.CharField(max_length=35)
        password2=models.CharField(max_length=35)



        def __str__(self):
            return self.username


class Register(models.Model):
    email = models.EmailField(max_length=55)
    username = models.CharField(max_length=30)
    password1 = models.CharField(max_length=35)
    password2 = models.CharField(max_length=35)

    def __str__(self):
        return self.username

class SpecialSlider(models.Model):
    slideImage=models.ImageField(upload_to='special_slider/')
    slideHeader=models.CharField(max_length=30)
    firsttitle=models.CharField(max_length=30)
    secoundtitle=models.CharField(max_length=30)
    productName=models.CharField(max_length=40)
    productDiscountPrice=models.DecimalField(max_digits=90,decimal_places=2)
    productOriginalPrice = models.DecimalField(max_digits=90, decimal_places=2)
    Buttontext=models.CharField(max_length=20)

class Tag(models.Model):
    name=models.CharField(max_length=100)

class BlogPost(models.Model):
        blogImage=models.ImageField(upload_to='blog/')
        blogheader=models.CharField(max_length=50)
        tags=models.ManyToManyField(Tag)
        blogeradminImage=models.ImageField(upload_to='blog/admin/')
        postdate=models.DateTimeField(auto_now=True)
        blogditails=models.TextField(max_length=500)


        # def get_recent_posts(self):
        #     return BlogPost.objects.filter(blogheader__in=self.blogheader)


class DealsOfTheDay(models.Model):
    productimage=models.ImageField(upload_to='ProductDeals/')
    targetdatetime=models.DateTimeField()
    productcategory=models.CharField(max_length=50)
    productname=models.CharField(max_length=50)
    productDiscountprice=models.DecimalField(max_digits=90,decimal_places=2)
    productOriginalprice=models.DecimalField(max_digits=90,decimal_places=2)
    productditails=models.CharField(max_length=50)
    buttontext=models.CharField(max_length=20)

class TopRatedProducts(models.Model):
    productimage = models.ImageField(upload_to='toprelatedProduct/')
    productcategory = models.CharField(max_length=50)
    productname = models.CharField(max_length=50)
    productDiscountprice = models.DecimalField(max_digits=90, decimal_places=2)
    productOriginalprice = models.DecimalField(max_digits=90, decimal_places=2)

class Banner(models.Model):
    bannerimage=models.ImageField(upload_to='banner/')
    firstline=models.CharField(max_length=50)
    secoundline=models.CharField(max_length=50)
    thirdline=models.CharField(max_length=50)
    fourthline=models.CharField(max_length=50)


class Carousel(models.Model):
    carousel=models.ImageField(upload_to='carousel/')


class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    message=models.TextField(max_length=200)

    def __str__(self):
        return self.name
class ProductsCategory(models.Model):
    name=models.CharField(max_length=50)
    icon=models.CharField(max_length=20)

    def __str__(self):
        return self.name

    @property
    def get_related(self):
        return self.related_set.all()

class Related(models.Model):
      category=models.ForeignKey(ProductsCategory,on_delete=models.CASCADE)
      productimage=models.ImageField(upload_to='Related/')
      productname=models.CharField(max_length=100)
      prodcutdiscountprice=models.DecimalField(max_digits=90,decimal_places=2,default=0.00)
      productoriginalprice=models.DecimalField(max_digits=90,decimal_places=2,default=0.00)
      productdescriptopm=models.CharField(max_length=100)

      def __str__(self):
          return self.productname


class bannerMovinImage(models.Model):
     movingimage=models.ImageField(upload_to='moveimage/')