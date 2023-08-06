from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.HomeView.as_view(),name='index'),
    path('home-<int:page_number>/', views.home_page, name='home_page'),
    path('login/',views.login_view,name='loginform' ),
    path('logout/',views.logout_view,name='logout' ),
    path('register/',views.RegisterView.as_view(),name='registerform'),
    path('blogPostditails/<int:blogger_id>',views.BlogditailsView.as_view(),name='blogditails'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('about-us/',views.AboutUs.as_view(),name='about-us'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)