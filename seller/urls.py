from django.urls import path
from .import views

app_name = 'seller'
urlpatterns = [
    path('SellerDashboard', views.sellerDashboard, name ='sellerDashboard'),
    path('sellerProfile', views.sellerProfile, name = 'sellerProfile'),
]
