from django.shortcuts import render
from .forms import categoryForm, subCategoryForm, shopForm, AddProductForm
from django.contrib import messages
from shop.models import Category, Sub_Category, Shop, Product, imageList, CustomUser
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def addCategory(request):
    catForm = categoryForm()
    if request.user.user_type == '1':
        base = 'owner/ownerDashboard.html'
    elif request.user.user_type == '2':
        base = 'seller/sellerDashboard.html'
    dist = {
        'form':catForm,
        'base':base,
    }
    if request.method == 'POST':
        form = categoryForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                savedata = form.save(commit = False)
                savedata.created_by = request.user
                savedata.save()
            except:
                messages.error(request, 'This Category has been added already!')
                return render(request, 'staff/addCategory.html', dist)
           
            messages.success(request, 'Category added Sucessfully')
            return HttpResponseRedirect(reverse('staff:viewYourCategory'))
        else:
            return render(request, "staff/addCategory.html", {'form':form,'base':base})
    else:
        return render(request, "staff/addCategory.html", dist)

def addSubCategroy(request):
    catForm = subCategoryForm()
    if request.user.user_type == '1':
        base = 'owner/ownerDashboard.html'
    elif request.user.user_type == '2':
        base = 'seller/sellerDashboard.html'
    dist = {
        'form':catForm,
        'base':base,
    }
    if request.method == 'POST':
        form = subCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                savedata = form.save(commit = False)
                savedata.created_by = request.user
                savedata.save()
            except:
                messages.error(request, 'This Sub Category has been added already!')
                return render(request, 'staff/addCategory.html', dist)
           
            messages.success(request, 'Sub Category added Sucessfully')
            return HttpResponseRedirect(reverse('staff:viewYourCategory'))
           
        else:
            return render(request, "staff/addSubCategroy.html", {'form':form,'base':base})
    else:
        return render(request, "staff/addSubCategroy.html", dist)
  

def addShop(request):
    catForm = shopForm()
    if request.user.user_type == '1':
        base = 'owner/ownerDashboard.html'
    elif request.user.user_type == '2':
        base = 'seller/sellerDashboard.html'
    dist = {
        'form':catForm,
        'base':base,
    }
    if request.method == 'POST':
        form = shopForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                savedata = form.save(commit = False)
                savedata.shop_owner = request.user
                savedata.save()
            except:
                messages.error(request, 'Please Contact Site admin for further details')
                return render(request, 'staff/addShop.html', dist)
            
            messages.success(request, 'Shop added Sucessfully')
            return HttpResponseRedirect(reverse('staff:yourShop'))
        else:
            return render(request, "staff/addShop.html", {'form':form,'base':base})
    else:
        return render(request, "staff/addShop.html", dist)
    
def yourShop(request):
    if request.user.user_type == '1':
        base = 'owner/ownerDashboard.html'
    elif request.user.user_type == '2':
        base = 'seller/sellerDashboard.html'
    yourshop = Shop.objects.filter(shop_owner=request.user)
    dist = {
        'shop': yourshop,
        'base':base
    }
    return render(request, "staff/staffShop.html", dist)

def addProduct(request):
    form = AddProductForm(request.POST or None, request.FILES or None)
    if request.user.user_type == '1':
        base = 'owner/ownerDashboard.html'
    else:
        base = 'seller/sellerDashboard.html'
    images = request.FILES.getlist("file[]")
    dist = {
        'form':form,
        'base':base,
    }
    if form.is_valid():
        aa = form.save(commit= False)
        aa.added_by = request.user
        aa.save()
        form.save_m2m()

        for img in images:
            image = imageList(product_id= aa, image= img)
            image.save()
        
        messages.success(request,"You have sucessfully added Product")
        return HttpResponseRedirect(reverse('staff:yourProduct'))
    else:
        return render(request, "staff/addProduct.html", dist)

    return render(request, "staff/addProduct.html", dist)

def viewYourProduct(request):
    if request.user.user_type == '1':
        base = 'owner/ownerDashboard.html'
    else:
        base = 'seller/sellerDashboard.html'
    product = Product.objects.filter(added_by=request.user)
    dist = {
        'product':product,
        'base':base,
    }
    return render(request, "staff/staffProductList.html", dist)

def viewYourCategory(request):
    if request.user.user_type == '1':
        base = 'owner/ownerDashboard.html'
    else:
        base = 'seller/sellerDashboard.html'
    yourCat = Category.objects.filter(created_by=request.user)
    subCat = Sub_Category.objects.filter(created_by = request.user)
    dist = {
        'yourCat':yourCat,
        'subCat':subCat,
        'base':base,
    }
    return render(request, 'staff/categoryList.html', dist)