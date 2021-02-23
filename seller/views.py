from django.shortcuts import render
from datetime import date
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from shop.models import CustomUser, Seller, Shop
from .forms import sellerEditForm

# Create your views here.
def sellerDashboard(request):
    time = date.today()
    shop = Shop.objects.filter(shop_owner = request.user)
    dist = {
        'time':time,
        'shop':shop,
    }
    return render(request, 'seller/sellerDashboard.html', dist)

def sellerProfile(request):
    real = Seller.objects.get(admin = request.user)
    form = sellerEditForm()
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
        'real':real,
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
            if match.id == request.user.id:
                aa = CustomUser.objects.get(id = request.user.id)
                aa.first_name = first_name
                aa.last_name = last_name
                own = Seller.objects.get(admin=request.user)
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
                messages.success(request, "Sucessfully updated profile")
                return HttpResponseRedirect(reverse('seller:sellerProfile'))
            else:
                messages.error(request, "This email is already Registered")
                return render(request, "seller/sellerProfile.html", {'form':form})
        except:
            aa = CustomUser.objects.get(id = request.user.id)
            aa.email = email
            aa.save()
            messages.success(request, "Sucessfully updated Email")
            return HttpResponseRedirect(reverse('seller:sellerProfile'))
    else:
        return render(request, 'seller/sellerProfile.html', dist)