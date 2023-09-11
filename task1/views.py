from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from task1.forms import RegisterForm,CommentForm,Loginform
from task1.models import Slider,  FolloUs,SecondSlider,Cart,CartItem,Comment,CommentAttachment,BlogPost, DealsOfTheDay, Category,Products ,Banner, Carousel, Contact,bannerMovinImage,SpecialOffer
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView,View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
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


    def get(self, request):
        if request.user.is_authenticated:
            # For authenticated users, retrieve the cart associated with their account
            cart = Cart.objects.get_or_create(user=request.user)[0]
            cart_items = CartItem.objects.filter(cart=cart)
        else:
            # For anonymous users, retrieve the session-based cart
            session_cart_id = request.session.get('cart_id')
            if session_cart_id:
                cart = Cart.objects.get_or_create(id=session_cart_id)[0]
                cart_items = CartItem.objects.filter(cart=cart)
            else:
                # Create a new session-based cart if one doesn't exist
                cart = Cart.objects.create()
                request.session['cart_id'] = cart.id
                cart_items = []

        total_prices = sum(item.quantity * item.product.price for item in cart_items)
        item_prices = [item.quantity * item.product.price for item in cart_items]
        cart_items_and_prices = zip(cart_items, item_prices)
        total_quantity = sum(item.quantity for item in cart_items)

        context = {
            'cart_items': cart_items,
            'cart_items_and_prices': cart_items_and_prices,
            'total_prices': total_prices,
            'total_quantity': total_quantity,
        }

        context.update(
            {
                'category': Category.objects.filter(subcategory=True),
                'product': Products.objects.filter(subcategory=True)
            }
        )

        return render(request, 'pages/shopping-cart.html', context=context)
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
             password=form.data['password']
             user=form.save()
             user.set_password(password)
             user.save()
             messages.success(request,'registrered successfully')
        else:
             messages.error(request,'Invalid Request')

        return render(request,'pages/register.html' ,{'form': form})

def logout_view(request):
    # if request.user.is_authenticated:
    #     request.user.cart.clear_cart()

        # Use Django's built-in logout function
    logout(request)

    return redirect('/')

    # user = request.user  # Get the user object
    #
    # if user.is_authenticated:
    #     # User is authenticated, access user.id or other user-related fields
    #     user_id = user.id
    # else:
    #     # User is not authenticated (AnonymousUser)
    #     user_id = None  # Ha
class  login_view(View):
    def get(self,request):
        return render(request, 'pages/login.html')

    def post(self,request):
        form=Loginform(request.POST)
        if form.is_valid():
            username=form.data['username']
            password=form.data['password']
            try:
               user=User.objects.get(username=username)
               if user.check_password(password):
                   login(request,user)
                   messages.success(request,'login succesfull')
               messages.error(request, 'password didnt match')
            except ObjectDoesNotExist:
                 messages.error(request,'user not found')
        else:
            print(form.errors)
            messages.error(request,"invalid error")

        return render(request, 'pages/login.html',{'form':form})

    # if request.method == 'POST':
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     user = authenticate(request, email=email, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('/')  # Redirect to the desired page
    # return render(request, 'pages/login.html')

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
            comment.user=User.objects.get(username=request.user.username)
            # attachment=attachment_form.save(commit=False)
            # attachment.comment = comment
            # attachment.save()
            comment.save()
        else:
            comment_form = CommentForm()
            # attachment_form = AttachmentForm()


        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)

    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user=user)
    else:
        session_cart_id = request.session.get('cart_id')
        if session_cart_id:
            cart, created = Cart.objects.get_or_create(id=session_cart_id)
        else:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    cart_item.quantity += 1
    cart_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class singleProduct(View):
    def get(self,request,product_id):
        product=Products.objects.get(id=product_id)

        context={
            'product':product,
        }
        return render(request,'pages/single-product.html')


def edit_cart_item(request,cart_item_id):
    cart_item=get_object_or_404(CartItem,id=cart_item_id)
    user = User.objects.get(username=request.user.username)
    if request.method=='POST':
        quantity=int(request.POST.get('quantity',1))

        if quantity>0:
            cart_item.quantity=quantity
            cart_item.save()
        return redirect('cart:cart')

    context={'cart_item':cart_item}
    return render(request,edit_cart_item())
def removecart(request,cart_item_id):
    try:
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.delete()
        # Redirect the user to a success page or another appropriate URL
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except CartItem.DoesNotExist:
        # Handle the case where the CartItem doesn't exist
        # You might want to return a 404 page or some other response
        return HttpResponse("CartItem not found", status=404)
    except Exception as e:
        # Handle other exceptions (e.g., database errors)
        # You can log the error for debugging purposes
        return HttpResponse("An error occurred", status=500)