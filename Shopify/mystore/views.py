from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.db import connection
from django.contrib import messages
from django.contrib.auth.models import User,auth
import json
from django.http import JsonResponse
# Create your views here.

def get_features(request):
    id = request.GET.get('id','')
    cat = categorie.objects.get(pk=id) 
    result = list(sub_categorie.objects.filter(catagory_name_id=cat).values('id', 'sub_name'))
    print(result)
    return HttpResponse(json.dumps(result), content_type="application/json") 

def home(request):
    ctgs = categorie.objects.all()
    sctgs = sub_categorie.objects.all()
    pros = Products.objects.all()
    brands = brand.objects.all()
    contex = {'ctgs':ctgs,'sctgs':sctgs, 'pros':pros, 'brands':brands}
    return render(request, 'home.html', contex)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complate = False)
        items = order.orderitem_set.all()
    else:
        items =[]
        order = {'get_cart_total':0}
    contex = {'items':items, 'order':order}    
    return render(request, 'cart.html', contex)


def Product_details(request, pk):
    ctgs = categorie.objects.all()
    sctgs = sub_categorie.objects.all()
    action = request.GET.get("action", None)
    Product = Products.objects.get(id=pk)
<<<<<<< HEAD
    brands = brand.objects.all()
    return render(request, 'product-details.html', {'ctgs': ctgs, 'sctgs': sctgs, 'Product': Product, 'brands':brands})
=======
    return render(request, 'product-details.html', {'ctgs': ctgs, 'sctgs': sctgs, 'Product': Product})
>>>>>>> 3c1fdefb67a7a8b958a6369e76672cf46e945534



def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complate = False)
        items = order.orderitem_set.all()
    else:
        items =[]
        order = {'get_cart_total':0}
    contex = {'items':items, 'order':order}
    if request.method == 'POST':
        Address = request.POST['Address']
        City = request.POST['City']
        State = request.POST['State']
        Country = request.POST['Country']

        shipping = ShippingAddress.objects.create(customer=customer,Order=order,Address=Address,city=City,state=State,country=Country)
        shipping.save()
        orderUp= Order.objects.filter(customer=customer).update(complate = True)
        return redirect('/')

    return render(request, 'checkout.html', contex)

def login_page(request):
    return render(request, 'login.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass2']
        pass2 = request.POST['pass2']

        user = User.objects.create_user(username=username,password = pass1, email=email, first_name = first_name, last_name=last_name)
        user.save()
        print('user created')
        return redirect('/')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def sub_ctg(request):
        sctg = sub_categorie.objects.all()
        return render(request, 'admin/mystore/change_form.html',{'sctg':sctg})

def product_by_cat(request, cname, sid):
    ctgs = categorie.objects.all()
    sctgs = sub_categorie.objects.all()
    ctg = categorie.objects.get(name = cname)
    pros = Products.objects.filter(ctg_id=ctg, sub_category_id = sid)
    brands = brand.objects.all()
    return render(request, 'product_by_cat.html',{'ctgs':ctgs,'sctgs':sctgs,'pros':pros,'brands':brands})

def BrandId(request,BrandId):
    ctgs = categorie.objects.all()
    sctgs = sub_categorie.objects.all()
    pros = Products.objects.filter(brand_name_id=BrandId)
    brands =brand.objects.all()
    return render(request, 'product_by_cat.html',{'ctgs':ctgs,'sctgs':sctgs,'pros':pros,'brands':brands})

def updateItem(request):
    data =json.loads(request.body)
    ProductId = data['ProductId']
    action = data['action']
    print(action)
    print(ProductId)

    customer = request.user
    Product = Products.objects.get(id=ProductId)
    order, created = Order.objects.get_or_create(customer=customer, complate = False)
    orderItem, created = OrderItem.objects.get_or_create(Order = order, Product = Product)

    if action == 'add':
        orderItem.Quantity = (orderItem.Quantity+1)
    elif action == 'remove':
        orderItem.Quantity = (orderItem.Quantity-1)
    
    orderItem.save()
    if orderItem.Quantity<=0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
