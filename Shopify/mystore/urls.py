from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'Home'),
    path('cart/', views.cart, name = 'cart'),
    path('login_page/', views.login_page, name = 'login_page'),
    path('login_page/login', views.login, name = 'login'),
    path('login_page/register', views.register, name = 'register'),
    path('logout', views.logout, name = 'logout'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('catDynamic', views.catDynamic, name = 'test'),
    path('features/',views.get_features,name='features'),
]