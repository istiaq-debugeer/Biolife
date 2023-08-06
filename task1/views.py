from django.contrib.auth import login, authenticate,logout
from django.contrib import messages


from task1 import forms
from task1.forms import RegisterForm,ContactForm
from task1.models import Slider, SpecialSlider, BlogPost, DealsOfTheDay, TopRatedProducts, Banner, Carousel, Contact,Related,ProductsCategory,bannerMovinImage
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View
def home_page(request, page_number):
    formatted_page_number = "{:02d}".format(page_number)
    return render(request, f'pages/home-{formatted_page_number}.html', {'page_number': page_number})

class AboutUs(TemplateView):
    template_name = 'pages/about-us.html'


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
        context['moving'] = bannerMovinImage.objects.all()

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




def logout_view(request):
    logout(request)
    return redirect('/')
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  # Redirect to the desired page
    return render(request, 'pages/login.html')





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


