from django.urls import path
from .import views
app_name = 'shop'
urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('login', views.loginView, name= 'login'),
    path('logout', views.logout_user, name = 'logout'),
    path('allCategory', views.allCategory, name="allCategory"),
    path("allService", views.allService, name = "allService"),
    path("allShop", views.allShop, name="allShop"),
    path('allProduct', views.allProduct, name = "allProduct"),
    path('productdetails/<slug:slug>/<int:id>', views.productDetails, name = 'productDetails'),
    path('shopProduct/<int:id>', views.shopProduct, name = 'shopProduct'),
    path('serviceProduct/<int:id>', views.serviceProduct, name = 'serviceProduct'),
    path('categorywise/<int:id>', views.categoryProduct, name ="categoryProduct"),
    path('loginpage', views.loginPage, name = "loginPage"),
    path('registerpage', views.signUp, name = "signup"),
]
