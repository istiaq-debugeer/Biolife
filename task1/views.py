from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from task1.forms import RegisterForm, ContactForm,CommentForm,CommentAttachment
from task1.models import Slider, SpecialSlider, BlogPost, DealsOfTheDay, Category,Products ,Banner, Carousel, Contact,bannerMovinImage,FolloUs,SpecialOffer
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,View

class home_page(TemplateView):


    def get(self,request,page_number, ):
            category = Category.objects.all()
            follow=FolloUs.objects.all()
            products=Products.objects.all()
            blog=BlogPost.objects.all()
            banner=Banner.objects.all()
            carousel=Carousel.objects.all()
            special=SpecialOffer.objects.all()
            formatted_page_number = "{:02d}".format(page_number)
            template=f'pages/home-{formatted_page_number}.html'

            context={
                'category':category,
                'blog':blog,
                'carousel':carousel,
                'follow':follow,
                'banner':banner,
                'special':special

            }
            return render(request, template,context=context)

    # def get_context_data(self,**kwargs):
    #         context = super().get_context_data(**kwargs)
    #         context['slider'] = Slider.objects.all()
    #         context['specialslider'] = SpecialSlider.objects.all()
    #         context['blog'] = BlogPost.objects.all()
    #         context['deals'] = DealsOfTheDay.objects.all()
    #         context['Toprated'] = TopRatedProducts.objects.all()
    #         context['banner'] = Banner.objects.all()
    #         context['carousel'] = Carousel.objects.all()
    #         context['contact'] = Contact.objects.all()
    #         context['relate'] = Related.objects.all()
    #         context['category'] = ProductsCategory.objects.all()
    #         context['moving'] = bannerMovinImage.objects.all()
    #
    #         return context

class AboutUs(TemplateView):
    template_name = 'pages/about-us.html'

class Blog(View):
    def get(self,request,page_number):

        blog=BlogPost.objects.all()
        recent_posts = BlogPost.objects.order_by('-postdate')[:3]
        formatted_page_number = "{:02d}".format(page_number)
        context = {
            'blog':blog,
            'recent_posts':recent_posts
        }

        template=f'pages/blog-v{formatted_page_number}.html'
        return render(request,template,context=context)

class Checkout(TemplateView):
    template_name = 'pages/checkout.html'

class ShoppingCart(TemplateView):
    template_name = 'pages/shopping-cart.html'

class Eror(TemplateView):
    template_name = 'pages/404.html'

class HomeView(TemplateView):
    template_name = 'index.html'




    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context.update(
            {
                'category':Category.objects.filter(subcategory=True),
                'products':Products.objects.filter(subcategory=True)
            }
        )
        context['slider']=Slider.objects.all()
        context['specialslider']=SpecialSlider.objects.all()
        context['blog']=BlogPost.objects.all()
        context['deals'] = DealsOfTheDay.objects.all()
        context['Toprated']=Products.objects.all()
        context['banner'] = Banner.objects.all()
        context['carousel']=Carousel.objects.all()
        context['contact'] = Contact.objects.all()
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
        recent_posts = BlogPost.objects.order_by('-postdate')[:3]
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





class post_comment(View):
    @login_required
    def post(self, request):

        comment_form = CommentForm(request.POST)
        # attachment_form=AttachmentForm(request.POST,request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save()
            # attachment=attachment_form.save(commit=False)
            # attachment.comment = comment
            # attachment.save()
            comment.save()
        else:
            comment_form = CommentForm()
            # attachment_form = AttachmentForm()
        return render(request, 'pages/blog-post.html', {'comment_form': comment_form})
#
