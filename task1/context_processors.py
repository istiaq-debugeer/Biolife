from .models import Category, Comment, BlogPost, Products, SecondSlider, Cart, CartItem, WebsiteSetting


def categories(request):
    return {"categories": Category.objects.all()}


def products(request):
    return {"products": Products.objects.all()}


def specialslider(request):
    return {"specialslider": SecondSlider.objects.all()}


def blogpost(request):

    return {"recents": BlogPost.objects.order_by('-postdate')[:3]}


def cart(request):

    return{"cart":Cart.objects.filter(user=user)}


def cartitem(request):
    if request.user.is_authenticated:
        user = request.user
        cart, _ = Cart.objects.get_or_create(user=user)
        cart_items = CartItem.objects.filter(cart=cart)
    else:
        user = None
        cart_items = None
    return {'cart_items': cart_items}


def websitesettings(request):
    return {"websitesettings": WebsiteSetting.objects.first()}


def Comments(request):
    return {"comments": Comment.objects.all()}


def cart_quantity(request):
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

    return {'total_quantity': total_quantity, 'total_prices': total_prices}
