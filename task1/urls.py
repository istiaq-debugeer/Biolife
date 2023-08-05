from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.HomeView.as_view(),name='index'),
    path('login/',views.loginView.as_view(),name='loginform' ),
    path('register/',views.RegisterView.as_view(),name='registerform'),
    path('blogPostditails/<int:blogger_id>',views.BlogditailsView.as_view(),name='blogditails'),
    path('contact/',views.ContactView.as_view(),name='contact'),

]