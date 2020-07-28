from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('cart', views.cart, name = 'cart'),
    path('product-details', views.Product_details, name = 'product-details'),
    path('login_page', views.login_page, name = 'login_page'),
    path('login', views.login, name = 'login'),
    path('register', views.register, name = 'register'),
    path('logout', views.logout, name = 'logout'),
    path('checkout', views.checkout, name = 'checkout'),
    path('updateItem/', views.updateItem, name = 'updateItem'),
    path('features/',views.get_features,name='features'),
    path('<str:cname>/<int:sid>', views.product_by_cat,name='products_by_cat')
]