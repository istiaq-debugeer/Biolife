from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from task1.forms import RegisterForm,CommentForm
from task1.models import Slider,  FolloUs,SecondSlider,User,Cart,CartItem,Comment,CommentAttachment,BlogPost, DealsOfTheDay, Category,Products ,Banner, Carousel, Contact,bannerMovinImage,SpecialOffer,Register
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView,View
from django.http import HttpResponseRedirect

class home_page(TemplateView):

    def get(self,request,page_number, ):

            follow=FolloUs.objects.all()
            # products=Products.objects.all()
            blog=BlogPost.objects.all()
            banner=Banner.objects.all()
            carousel=Carousel.objects.all()
            special=SpecialOffer.objects.all()
            formatted_page_number = "{:02d}".format(page_number)
            template=f'pages/home-{formatted_page_number}.html'
            cart_items = CartItem.objects.all ( )


            total_prices = sum ( item.quantity * item.product.price for item in cart_items )

            item_prices = [item.quantity * item.product.price for item in cart_items]
            cart_items_and_prices = zip ( cart_items, item_prices )

            total_quantity = sum ( item.quantity for item in cart_items )


            context = {
                'cart_items': cart_items,
                'cart_items_and_prices': cart_items_and_prices,
                'total_prices': total_prices,
                'total_quantity': total_quantity,

            }

            context={

                'blog':blog,
                'carousel':carousel,
                'follow':follow,
                'banner':banner,
                'special':special,


            }
            return render(request, template,context=context)



class AboutUs(TemplateView):
    template_name = 'pages/about-us.html'

class Blog(View):
    def get(self,request,page_number):

        blog=BlogPost.objects.all()
        recent_posts = BlogPost.objects.order_by('-postdate')[:3]
        formatted_page_number = "{:02d}".format(page_number)
        context = {
            'blog':blog,
            'recent_posts':recent_posts,
            # 'category': Category.objects.filter ( subcategory=True ),
            # 'products': Products.objects.filter ( subcategory=True )
        }

        template=f'pages/blog-v{formatted_page_number}.html'
        return render(request,template,context=context)

class Checkout(TemplateView):
    template_name = 'pages/checkout.html'

class ShoppingCart(View):

    def get(self,request):

    # def get_context_data ( self, **kwargs ):
    #     context = super ( ).get_context_data ( **kwargs )
    #     context.update (
    #         {
    #             'category': Category.objects.filter ( subcategory=True ),
    #             'product': Products.objects.filter ( subcategory=True )
    #         }
    #     )
    #     return context


        # cart = Cart.objects.get(user=request.user)
        cart_items = CartItem.objects.all ( )
        print ( 'cartitem:', cart_items )

        total_prices = sum ( item.quantity * item.product.price for item in cart_items )

        item_prices = [item.quantity * item.product.price for item in cart_items]
        cart_items_and_prices = zip ( cart_items, item_prices )

        total_quantity = sum ( item.quantity for item in cart_items )

        print ( total_prices )
        context = {
            'cart_items': cart_items,
            'cart_items_and_prices': cart_items_and_prices,
            'total_prices': total_prices,
            'total_quantity': total_quantity,

        }

        context.update (
                 {
                     'category': Category.objects.filter ( subcategory=True ),
                    'product': Products.objects.filter ( subcategory=True )
                 }
             )
        return render ( request, 'pages/shopping-cart.html', context=context )

class Eror(TemplateView):
    template_name = 'pages/404.html'

class HomeView(TemplateView):
    template_name = 'index.html'



    def get_context_data(self, **kwargs):


        context=super().get_context_data(**kwargs)
        context.update(
            {
                'category':Category.objects.filter(subcategory=True),
                'product':Products.objects.filter(subcategory=True)
            }
        )

        context['slider']=Slider.objects.all()
        context['specialslider']=SecondSlider.objects.all()
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
            user=form.save()

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

    def get(self,request,blogger_id):
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

    @method_decorator(login_required)
    def post(self, request):

        comment_form = CommentForm(request.POST)
        # attachment_form=AttachmentForm(request.POST,request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user=Register.objects.get(username=request.user.username)
            # attachment=attachment_form.save(commit=False)
            # attachment.comment = comment
            # attachment.save()
            comment.save()
        else:
            comment_form = CommentForm()
            # attachment_form = AttachmentForm()


        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(Products, id=product_id)

    user=Register.objects.get(username=request.user.username)
    print('user:',user)
    cart, created = Cart.objects.get_or_create(user=user)
    print("Cart created:",created)
    cart_item ,created= CartItem.objects.get_or_create(cart=cart, product=product)

    print ( "Cart created:",cart_item )
    cart_item.quantity += 1

    print ( "quantity:", cart_item.quantity )
    cart_item.save()

    return HttpResponseRedirect('/')


class singleProduct(View):
    def get(self,request,product_id):
        product=Products.objects.get(id=product_id)

        context={
            'product':product,
        }
        return render(request,'pages/single-product.html')


def edit_cart_item(request,cart_item_id):
    cart_item=get_object.or_404(CartItem,id=cart_item_id)

    if request.method=='POST':
        quantity=int(request.POST.get('quantity',1))

        if quantity>0:
            cart_item.quantity=quantity
            cart_item.save()
        return redirect('cart:cart')

    context={'cart_item':cart_item}
    return render(request,edit_cart_item())