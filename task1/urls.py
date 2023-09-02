from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.HomeView.as_view(),name='index'),
    path('home-<int:page_number>/', views.home_page.as_view(), name='home_page'),
    path('login/',views.login_view,name='loginform' ),
    path('logout/',views.logout_view,name='logout' ),
    path('register/',views.RegisterView.as_view(),name='registerform'),
    path('blogPostditails/<int:blogger_id>',views.BlogditailsView.as_view(),name='blogditails'),
    path('blog-<int:page_number>/', views.Blog.as_view(), name='blog_page'),
    path('comment/',views.post_comment.as_view(),name='comment'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('checkout/',views.Checkout.as_view(),name='checkout'),
    path('cart/',views.ShoppingCart.as_view(),name='cart'),
    path('404/',views.Eror.as_view(),name='error'),
    path('about-us/',views.AboutUs.as_view(),name='about-us'),
    path('add-to-cart/<int:product_id>/',views.add_to_cart,name='add-to-cart'),
    path('productditails/<int:product_id>/',views.singleProduct.as_view(),name='singleproductview'),

    # path ( 'cart/', views.cart_view, name='cart' ),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)