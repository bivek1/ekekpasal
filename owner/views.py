from django.shortcuts import redirect, render
from datetime import date
from shop.models import Category, Sub_Category,Service, CustomUser, Seller, Owner, Product, Shop,totalVisit
from staff.forms import serviceForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import SellerForm, OwnerEditForm
from seller.forms import sellerEditForm

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
    shop = Shop.objects.filter(shop_owner = request.user)
    dist = {
        'time':time,
        'pt':PT,'st':ST,'set':SeT, 'sh':SH, 'cat':cat, 'sub':sub, 'visit':visit,
        'shop': shop,
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
        TypeOne.seller.added_by = request.user.username
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

def editService(request, id):
    service = Service.objects.get(id = id)
    dist = {
        's':service
    }
    if request.method =='POST' or request.method == 'FILES':
        try:
            service.service_name = request.POST['service_name']
            if request.FILES.get('image', False):
                service.image = request.FILES['image']
                service.save()
            else:
                service.save()
            messages.success(request, "Sucessfully Updated Service")
            return HttpResponseRedirect(reverse('owner:editService', args=[service.id]))
        except:   
            messages.success(request, "Something went Wrong")
            return HttpResponseRedirect(reverse('owner:editService', args=[service.id]))
    return render(request, "owner/editService.html", dist)


def editSeller(request, id):
    form = sellerEditForm()
    real = Seller.objects.get(id = id)
    form.fields['email'].initial = real.admin.email
    form.fields['first_name'].initial = real.admin.first_name
    form.fields['last_name'].initial = real.admin.last_name
    form.fields['Temporary_address'].initial = real.Temporary_address
    form.fields['number'].initial = real.number
    form.fields['District'].initial = real.District
    form.fields['street'].initial = real.street
    form.fields['gender'].initial = real.gender
    form.fields['KYC'].initial = real.KYC
    
    dist = {
        'form':form,
        's':real,
    }
   
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        Temporary_address = request.POST['Temporary_address']
        number = request.POST['number']
        District = request.POST['District']
        street = request.POST['street']
        gender = request.POST['gender']
        try:
            kyc = request.FILES['KYC']
        except:
            kyc = None
        
        try:
            match = CustomUser.objects.get(email=email)
            if match.id == real.admin.id:
                aa = CustomUser.objects.get(id = real.admin.id)
                aa.first_name = first_name
                aa.last_name = last_name
                own = Seller.objects.get(admin=real.admin.id)
                own.Temporary_address = Temporary_address
                own.number = number
                own.District = District
                own.street = street
                own.gender = gender
                if kyc:
                    own.KYC = kyc
                else:
                    pass
                own.save()
                aa.save()
                messages.success(request, "Sucessfully updated Seller")
                return HttpResponseRedirect(reverse('owner:editSeller' , args=[real.id]))
            else:
                messages.error(request, "This email is already Registered")
                return render(request, "owner/editSeller.html", dist)
        except:
            aa = CustomUser.objects.get(id = real.admin.id)
            aa.email = email
            aa.save()
            messages.success(request, "Sucessfully updated Email")
            return HttpResponseRedirect(reverse('owner:editSeller', args=[real.id]))
    else:
        return render(request, "owner/editSeller.html", dist)

def viewSeller(request, id):
    seller = Seller.objects.get(id = id)
    shop = Shop.objects.filter(shop_owner = seller.admin.id)
    product = Product.objects.filter(added_by = seller.admin.id)
    shop_count = Shop.objects.filter(shop_owner = seller.admin.id).count()
    product_count = Product.objects.filter(added_by = seller.admin.id).count()
    dist = {
        's':seller,
        'shop':shop,
        'product':product,
        'c':shop_count,
        'p':product_count,
    }
    
    return render(request, "owner/viewSeller.html", dist)