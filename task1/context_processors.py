from .models import Category,Comment,BlogPost,Products,SecondSlider,Cart,CartItem,WebsiteSetting

def categories(request):
    return{"categories":Category.objects.all()}

def products(request):
    return {"products":Products.objects.all()}

def specialslider(request):
    return {"specialslider":SecondSlider.objects.all()}


def blogpost(request):
    return {"recents":BlogPost.objects.order_by('-postdate')[:3]}

def cart(request):
    return {"cart":Cart.objects.all()}

def cartitem(request):
    return {"cartitem":CartItem.objects.all()}

def websitesettings(request):
    return {"websitesettings":WebsiteSetting.objects.first()}

def Comments(request):
    return{"comments":Comment.objects.all()}