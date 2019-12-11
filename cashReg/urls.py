from django.urls import path
from . import views as core_views
from . import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^product/entry/$', core_views.AddProductView, name='product-entry'),
    url(r'^list/$', views.ProductListView.as_view(), name='list'),
    url(r'^cart/$', views.Cartview, name='cart'),
    path('cart/<int:pk>/view/', views.update_cart, name='update_cart'),
    url(r'^thankyou/$', views.ThankYou, name='thankyou'),
]
