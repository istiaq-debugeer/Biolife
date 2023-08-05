
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View

from task1 import forms
from task1.forms import RegisterForm,ContactForm

from task1.models import Slider, SpecialSlider, BlogPost, DealsOfTheDay, TopRatedProducts, Banner, Carousel, Contact,Related,ProductsCategory



# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'



    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['slider']=Slider.objects.all()
        context['specialslider']=SpecialSlider.objects.all()
        context['blog']=BlogPost.objects.all()
        context['deals'] = DealsOfTheDay.objects.all()
        context['Toprated']=TopRatedProducts.objects.all()
        context['banner'] = Banner.objects.all()
        context['carousel']=Carousel.objects.all()
        context['contact'] = Contact.objects.all()
        context['relate'] = Related.objects.all()
        context['category'] = ProductsCategory.objects.all()

        return context


class RegisterView(View):
    def get(self,request):
        return render(request,'pages/register.html')

    def post(self,request):
        form=RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your message sents successfully')

        else:
            messages.error(request,'Invalid Request')

        return render(request,'pages/register.html')



class loginView(TemplateView):
        template_name = 'pages/login.html'



from django.shortcuts import render
from .models import BlogPost


class BlogditailsView(View):

    def get(sel,request,blogger_id):
        blog=BlogPost.objects.get(id=blogger_id)
        recent_posts = BlogPost.objects.order_by('-postdate')[:10]
        context={
            'blog':blog,
            'recent_posts': recent_posts,
        }

        return render(request,'pages/blog-post.html',context=context)


class ContactView(View):
    def get(self,request):
        return render(request,'pages/contact.html')

    def post(self,request):
        form=ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your message sents successfully')
        else:
            messages.error(request,'Invalid Request')

        return render(request,'pages/contact.html')


