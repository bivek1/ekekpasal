from django.contrib import admin
from .models import CustomUser, Product, Owner, Seller,imageList, Delivery, Shop, Customer, Delivery_address, Brand, Category, Sub_Category, Service
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Owner)
admin.site.register(Seller)
admin.site.register(Delivery)
admin.site.register(Delivery_address)
admin.site.register(Customer)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Service)
admin.site.register(Shop)
admin.site.register(imageList)
