from django.shortcuts import redirect, render
from datetime import date
from shop.models import Category, Sub_Category,Service, CustomUser, Seller, Owner, Product, Shop,totalVisit
from staff.forms import serviceForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import SellerForm, OwnerEditForm

# Create your views here.
def AdminDashboard(request):
    PT = Product.objects.all().count()
    ST = Seller.objects.all().count
    SeT = Service.objects.all().count
    SH = Shop.objects.all().count()
    cat = Category.objects.all().count()
    sub = Sub_Category.objects.all().count()
    time = date.today()
    visit = totalVisit.objects.all().count()
    dist = {
        'time':time,
        'pt':PT,'st':ST,'set':SeT, 'sh':SH, 'cat':cat, 'sub':sub, 'visit':visit,
    }
    return render(request, "owner/ownerDashboard.html",dist)

def addService(request):
    form = serviceForm()
    dist = {
        'form':form
    }
    if request.method == "POST":
        form = serviceForm(request.POST, request.FILES)
        if form.is_valid():
        # try:
            form.save()
            messages.success(request, "Service Added sucessfully")
            return HttpResponseRedirect(reverse("shop:allService"))
        # except:
        #     messages.error(request, "This Service has been added already")
        #     return HttpResponseRedirect(reverse("owner:addService"))
    else:
        return render(request, "owner/addService.html", dist)

def manageService(request):
    service = Service.objects.all()
    return render(request, "owner/manageService.html", {'service':service})

def addSeller(request):
    form = SellerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        cd = form.cleaned_data
        first_name = cd['first_name']
        last_name = cd['last_name']
        email = cd['email']
        password = cd['password']
        number = cd['number']
        city = cd['Temporary_address']
        district = cd['District']
        gender = cd['gender']
        kyc = cd['KYC']
        street = cd['street']
        TypeOne = CustomUser.objects.create_user(first_name=first_name, last_name = last_name, email = email, username = email, password=password, user_type = "2")
        TypeOne.seller.number=number
        TypeOne.seller.Temporary_address=city
        TypeOne.seller.street=street
        TypeOne.seller.District= district
        TypeOne.seller.gender=gender
        TypeOne.seller.KYC = kyc
        TypeOne.seller.verified = True
        TypeOne.seller.save()
        return HttpResponseRedirect(reverse('owner:sellerList'))
    else:
        return render(request, "owner/addSeller.html", {'form':form})
    return render(request, "owner/addSeller.html", {'form':form})

def sellerList(request):
    seller = Seller.objects.all()
    dist = {
        'seller':seller
    }
    return render(request, 'owner/sellerList.html', dist)

def yourProfile(request):
    real = Owner.objects.get(admin = request.user)
    form = OwnerEditForm()
    form.fields['email'].initial = real.admin.email
    form.fields['first_name'].initial = real.admin.first_name
    form.fields['last_name'].initial = real.admin.last_name
    form.fields['address'].initial = real.address
    dist = {
        'form':form,
    }
   
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        address = request.POST['address']
        try:
            match = CustomUser.objects.get(email=email)
            if match.id == request.user.id:
                aa = CustomUser.objects.get(id = request.user.id)
                aa.first_name = first_name
                aa.last_name = last_name
                own = Owner.objects.get(admin=request.user)
                own.address = address
                own.save()
                aa.save()
                messages.success(request, "Sucessfully updated profile")
                return HttpResponseRedirect(reverse('owner:yourProfile'))
            else:
                messages.error(request, "This email is already Registered")
                return render(request, "owner/OwnerProfile.html", {'form':form})
        except:
            aa = CustomUser.objects.get(id = request.user.id)
            
            aa.email = email
            
        
            aa.save()
            messages.success(request, "Sucessfully updated Email")
            return HttpResponseRedirect(reverse('owner:yourProfile'))
    else:
        return render(request, "owner/OwnerProfile.html", dist)

def manageSite(request):
    return render(request, "owner/manageSite.html")

