from django.urls import path
from .import views

app_name = "owner"
urlpatterns = [
    path('admindashboard', views.AdminDashboard, name="AdminDashboard"),
    path('addService', views.addService, name= "addService"),
    path('manageService', views.manageService, name = "manageService"),
    path('addSeller', views.addSeller, name = "addSeller"),
    path('sellerList', views.sellerList, name = 'sellerList'),
    path('YourProfile', views.yourProfile, name = "yourProfile"),
    path('manageSite', views.manageSite, name= "manageSite"),
  
]
