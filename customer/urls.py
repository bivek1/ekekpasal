from django.urls import path
from .import views
app_name = 'customer'

urlpatterns = [
    path('customerdashboard', views.customerDashboard, name ="customerDashboard"),
]
