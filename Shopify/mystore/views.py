from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import categorie,sub_categorie
from django.db import connection
from django.contrib import messages
from django.contrib.auth.models import User,auth
import json
# Create your views here.


def get_features(request):
    id = request.GET.get('id','')
    cat = categorie.objects.get(pk=id) 
    result = list(sub_categorie.objects.filter(catagory_name_id=cat).values('id', 'name')) 
    print(result)
    return HttpResponse(json.dumps(result), content_type="application/json") 

def home(request):
    ctgs = categorie.objects.all()
    sctgs = sub_categorie.objects.all()
    return render(request, 'index.html',{'ctgs':ctgs,'sctgs':sctgs})

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

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
        user.save();
        print('user created')
        return redirect('/')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def catDynamic(request):
    ctg = categorie.objects.all()
    sctg = sub_categorie.objects.all()
    return render(request,'dynamictest.html', {'ctg': ctg ,'sctg': sctg })

def sub_ctg(request):
        sctg = sub_categorie.objects.all()
        return render(request, 'admin/categories.html',{'sctg':sctg})