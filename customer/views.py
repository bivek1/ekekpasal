from django.shortcuts import render
from shop.models import Service
# Create your views here.
def customerDashboard(request):
    return render(request,"customer/customerDashboard.html")

def selectService(request):
    service = Service.objects.all()
    dist = {
        'service': service
    }
    return render(request, "customer/selectService.html", dist)

def selectInterst(request):
    return render(request, "customer/selectInterest.html")