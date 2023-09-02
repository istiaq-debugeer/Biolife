from django.contrib import admin
from django import forms
from task1.models import Slider,User,SecondSlider,BlogPost,Tag,DealsOfTheDay,Banner,Carousel,Contact,Register,bannerMovinImage,Contact,FolloUs,Cart,CartItem,Comment,CommentAttachment,WebsiteSetting,SpecialOffer,Products,Category

# Register your models here.
admin.site.register(Slider)
admin.site.register(Register)
admin.site.register(SecondSlider)
admin.site.register(BlogPost)
admin.site.register(Tag)
admin.site.register(DealsOfTheDay)
admin.site.register(Products)
admin.site.register(Banner)
admin.site.register(Carousel)
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Category)

admin.site.register(bannerMovinImage)
admin.site.register(Comment)
admin.site.register(FolloUs)
admin.site.register(SpecialOffer)
admin.site.register(WebsiteSetting)
admin.site.register(Cart)
admin.site.register(CartItem)





