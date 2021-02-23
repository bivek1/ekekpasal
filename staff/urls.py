from django.urls import path
from .import views

app_name = "staff"

urlpatterns = [
    path('addcategory', views.addCategory, name="addCategory"),
    path("addSubCategory", views.addSubCategroy, name= "addSubCategory"),
    path('addShop', views.addShop, name = "addShop"),
    path('addProduct', views.addProduct, name = "addProduct"),
    path('yourshop', views.yourShop, name = 'yourShop'),
    path('viewYourCategory', views.viewYourCategory, name = 'viewYourCategory'),
    path('YourProduct', views.viewYourProduct, name="yourProduct"),
    path('edit/<int:id>', views.editShop, name="editShop"),

]
