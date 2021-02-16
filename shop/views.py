from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Category, Sub_Category, Service, Product, Shop
from shop.models import CustomUser
from django.core.mail import message
from django.core.paginator import Paginator

# Create your views here.
def homepage(request):
    service = Service.objects.all()
    shop = Shop.objects.all()
    product = Product.objects.all()
    paginator = Paginator(product, 12)
    page = request.GET.get('page')
    print(page)
    try:
        aa = int(page)
    except:
        aa = 1
    print(type(aa))
    print(type(page))
    memData = paginator.page(aa)
    dist = {
        'service':service,
        'shop':shop,
        'product':memData,
        'category':Category.objects.all()
    }
    return render(request, 'shop/index.html', dist)

def loginPage(request):
    return render(request, "shop/loginPage.html")


def loginView(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user!= None:
            login(request, user)
            if user.user_type == "1":
                return HttpResponseRedirect(reverse("owner:AdminDashboard"))
            if user.user_type == "2":
                return HttpResponseRedirect(reverse("seller:sellerDashboard"))
            if user.user_type == "3":
                return HttpResponseRedirect(reverse("customer:customerDashboard"))
            else:
                return HttpResponseRedirect(reverse("customer_page"))
        else:
            messages.error(request, "Invalid Login Credential")
            return HttpResponseRedirect(reverse('shop:loginPage'))
    else:
        return HttpResponseRedirect(reverse('shop:homepage'))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('shop:homepage'))

def signUp(request):
    if request.method == 'POST':
        email = request.POST['email']
        passw = request.POST['passw']
        passw2 = request.POST['password2']
        if passw == passw2:
            TypeOne = CustomUser.objects.create_user(email = email, username = email, password=passw, user_type = "3")
            messages.success(request, "Sign Up sucessfull. Please Login")
            return HttpResponseRedirect(reverse('shop:loginPage'))
        else:
            messages.error(request, "Password Does not match")
            return render(request, "shop/register.html")
    else:
        return render(request, "shop/register.html")

def allCategory(request):
    all_cat = Category.objects.all()
    dist = {
        'allcat':all_cat,
        'category':Category.objects.all()
    }
    return render(request, "shop/allCategory.html", dist)

def allService(request):
    service = Service.objects.all()
    dist = {
        'service':service,
        'category':Category.objects.all()
    }
    return render(request, "shop/allService.html",dist)

def allShop(request):
    shop = Shop.objects.all()
    dist = {
        'shop':shop,
        'category':Category.objects.all()
    }
    return render(request, "shop/allShop.html", dist)

def allProduct(request):
    dist = {
        'product' : Product.objects.all(),
        'category':Category.objects.all()
    }
    return render(request, "shop/allProduct.html", dist)

def productDetails(request, slug, id):
    product = Product.objects.get(id = id)
    shop = product.from_shop
    count = Product.objects.filter(from_shop = shop).count()
    similar_product = Product.objects.filter(sub_category= product.sub_category).exclude(id = id)
    print(shop)
    dist = {
        'p':product,
        'count':count,
        'similar_product':similar_product,
        'category':Category.objects.all()
    }
    return render(request, "shop/productDetails.html", dist)
    
def shopProduct(request, id):
    shop = Shop.objects.get(id = id)
    product = Product.objects.filter(from_shop = shop)
    dist = {
        'product': product,
        's':shop,
        'category':Category.objects.all()
    }
    return render(request, "shop/shopProduct.html", dist)

def serviceProduct(request, id):
    service = Service.objects.get(id = id)
    product = Product.objects.filter(service = service)
    dist = {
        'product': product,
        's':service,
        'category':Category.objects.all()
    }
    return render(request, "shop/serviceProduct.html", dist)

def categoryProduct(request, id):
    category = Category.objects.get(id = id)
    product = Product.objects.filter(category = category)
    dist = {
        'product': product,
        's':category,
        
    }
    return render(request, "shop/serviceProduct.html", dist)