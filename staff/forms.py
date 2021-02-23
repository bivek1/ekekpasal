from django import forms
from shop.models import Category, Sub_Category,Product, Shop, Service
from django.core.exceptions import ValidationError
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
            'service',
            'image',
        )
        labels = {
            'name': 'Category Name',
            'service': 'Service Name',
            'image': 'Category Image',
        }
        widgets = {
            'name': forms.TextInput(attrs = {'placeholder' :' Add Category', 'class':'form-control'}),
            'service': forms.Select(attrs = {'class':'form-control'}),
            'image': forms.FileInput(attrs= {'class':'form-control'}),
        }
        def clean_name(self):
            data = self.cleaned_data['name']
            try:
                check = data.lower()
                same = Category.objects.get(name = check)
            except:
                return data
            raise ValidationError('This Category is added already')
        
class subCategoryForm(forms.ModelForm):
    class Meta:
        model = Sub_Category
        fields = (
            'sub_name',
            'category',
            'image',
        )
        labels = {
            'sub_name': 'Sub Category Name',
            'category': 'Category Name',
            'image': 'Sub Category Image',
        }
        widgets = {
            'sub_name': forms.TextInput(attrs = {'placeholder' :' Add Sub Category', 'class':'form-control'}),
            'category': forms.Select(attrs = {'class':'form-control'}),
            'image': forms.FileInput(attrs= {'class':'form-control'}),
        }
        
class serviceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = (
            'service_name',
            'image',
        )
        labels = {
            'service_name': 'Service Name',
            'image': 'Sub Category Image',
        }
        widgets = {
            'service_name': forms.TextInput(attrs = {'placeholder' :' Add Service', 'class':'form-control'}),
            'image': forms.FileInput(attrs= {'class':'form-control'}),
        }
        
        def clean_service_name(self):
            data = self.cleaned_data['service_name']
            try:
                check = data.lower()
                same = Service.objects.get(service_name = check)
            except:
                return data
            raise ValidationError('This Service is added already')
        
class shopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = (
            'shop_name',
            'VAT',
            'address',
            'shop_number',
            'image',
            'service_provide',
        )
        labels = {
            'shop_name': "Shop Name",
            'VAT': "Vat/Pan No. of the shop",
            'address': "Address of the Shop",
            'shop_number': "Shop Number/Vendor Number",
            'image':'Image of Shop',
            'service_provide':'Service of the Shop',
        }
        widgets = {
            'shop_name':forms.TextInput(attrs={'class':"form-control", "placeholder":"Shop Name"}),
            'VAT':forms.TextInput(attrs={'class':"form-control", "placeholder":"VAT or PAN Number"}),
            'address':forms.TextInput(attrs={'class':"form-control", "placeholder":"Address"}),
            'shop_number':forms.NumberInput(attrs={'class':"form-control", "placeholder":"Shop Number"}),
            'image':forms.FileInput(attrs={'class':"form-control"}),
            'service_provide':forms.Select(attrs={'class':'form-control'})
        }
class editShopForm(forms.Form):
    shop_name = forms.CharField(max_length= 200, label = "Shop Name", widget= forms.TextInput(attrs={'class':'form-control', 'placeholder':'Shop Name'}))
    VAT = forms.CharField(max_length = 200, label = "VAT", widget = forms.TextInput(attrs= {'class':'form-control', 'placeholder':'VAT/ PAN No.'}))
    address = forms.CharField(max_length = 200, label = "Address", widget = forms.TextInput(attrs= {'class':'form-control', 'placeholder':'Shop Address'}))
    image = forms.ImageField(max_length = 200, label = "Image", widget = forms.FileInput(attrs= {'class':'form-control', 'placeholder':'Shop Address'}))
    shop_number = forms.CharField(max_length = 10, label = "Shop Number", widget = forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Shop Number'}))
    service = []
    ser = Service.objects.all()
    try:
        for s in ser:
            cat = (s.id , s.service_name)   
            service.append(cat) 
    except:
        service = []
    service_provide = forms.ChoiceField(label = "Service of Shop", choices =  service, widget = forms.Select(attrs= {'class':'form-control'}))


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category','sub_category', 'size' ,'service','from_shop','short','discount','image','description','price','available_quantity','available','tags','cashpayment','features','sale','sponsor','allovernepal')
        labels = {
            'name': 'Product Name',
            'category':'Product Category',
            'sub_category':'Product Sub-Category',
            'short':'Short Description',
            'commision':'Commision rate for Affilite',
            'discount':'Discount Percentage',
            'size': "Available Size",
            'image':'Thumbnail Image',
            'description':'Full Details Decrition',
            'price':'Product Prices',
            'service':'Product Service',
            'available_quantity':'Available Quantity',
            'available':'Product Available or not?',
            'tags':'Products Tags',
            'cashpayment':'CashPayment Acceptable?',
            'features':'Featured Product?',
            'sale':'Sale Type',
            'from_shop': 'Shop of the Product',
            'sponsor':'Sponsored or Not?',
            'allovernepal':'Delivery all over Nepal?',
        }
        
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Product Name'}),
            'size': forms.TextInput(attrs={'class':'form-control', 'placeholder':'L, XL, M, S'}),
            'category':forms.Select(attrs={'class':'form-control', 'placeholder':'Product Category'}),
            'sub_category':forms.Select(attrs={'class':'form-control', 'placeholder':'Product Sub Category'}),
            'short':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Short Description'}),
            'commision':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Commision on Product'}),
            'discount':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Discount on Product'}),
            'service':forms.Select(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'description':CKEditorUploadingWidget(),
            'from_shop': forms.Select(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Product Price'}),
            'available_quantity':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Available Quality'}),
            'available':forms.CheckboxInput(attrs= {'class':'form-check-input'}),
            'tags':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Product Tags'}),
            'cashpayment':forms.CheckboxInput(attrs= {'class':'form-check-input'}),
            'features':forms.CheckboxInput(attrs= {'class':'form-check-input'}),
            'sale':forms.Select(attrs={'class':'form-control'}),
            'sponsor':forms.CheckboxInput(attrs= {'class':'form-check-input'}),
            'allovernepal':forms.CheckboxInput(attrs= {'class':'form-check-input'})
        }