from django.shortcuts import render

# Create your views here.
def customerDashboard(request):
    return render(request,"customer/customerDashboard.html")