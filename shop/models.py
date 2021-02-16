from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
from ckeditor_uploader.fields import RichTextUploadingField

district = (
    ('Taplejung','Taplejung'),
    ('Panchthar','Panchthar'),
    ('Ilam','Ilam'),
    ('Jhapa','Jhapa'),
    ('Morang','Morang'),
    ('Sunsari','Sunsari'),
    ('Dhankutta','Dhankutta'),
    ('Sankhuwasabha','Sankhuwasabha'),
    ('Bhojpur','Bhojpur'),
    ('Okhaldunga','Okhaldunga'),
    ('Khotang','Khotang'),
    ('Solukhumbu','Solukhumbu'),
    ('Udaypur','Udaypur'),
    ('Saptari','Saptari'),
    ('Siraha','Siraha'),
    ('Dhanusa','Dhanusa'),
    ('Mahottari','Mahottari'),
    ('Sarlahi','Sarlahi'),
    ('Sindhuli','Sindhuli'),
    ('Ramechhap','Ramechhap'),
    ('Dolkha','Dolkha'),
    ('Sindhupalchauk','Sindhupalchauk'),
    ('Kavreplanchauk','Kavreplanchauk'),
    ('Lalitpur','Lalitpur'),
    ('Bhaktapur','Bhaktapur'),
    ('Kathmandu','Kathmandu'),
    ('Nuwakot','Nuwakot'),
    ('Rasuwa','Rasuwa'),
    ('Dhading','Dhading'),
    ('Makwanpur','Makwanpur'),
    ('Rauthat','Rauthat'),
    ('Parsa','Parsa'),
    ('Chitwan','Chitwan'),
    ('Gorkha','Gorkha'),
    ('Lamjung','Lamjung'),
    ('Tanahun','Tanahun'),
    ('Syangja','Syangja'),
    ('Kaski','Kaski'),
    ('Manag','Manag'),
    ('Mustang','Mustang'),
    ('Parwat','Parwat'),
    ('Myagdi','Myagdi'),
    ('Baglung','Baglung'),
    ('Gulmi','Gulmi'),
    ('Palpa','Palpa'),
    ('Nawalparasi','Nawalparasi'),
    ('Rupandehi','Rupandehi'),
    ('Arghakhanchi','Arghakhanchi'),
    ('Kapilvastu','Kapilvastu'),
    ('Pyuthan','Pyuthan'),
    ('Rukum','Rukum'),
    ('Rolpa','Rolpa'),
    ('Salyan','Salyan'),
    ('Dang','Dang'),
    ('Bardiya','Bardiya'),
    ('Surkhet','Surkhet'),
    ('Dailekh','Dailekh'),
    ('Banke','Banke'),
    ('Jajarkot','Jajarkot'),
    ('Dolpa','Dolpa'),
    ('Humla','Humla'),
    ('Kalikot','Kalikot'),
    ('Mugu','Mugu'),
    ('Jumla','Jumla'),
    ('Bajura','Bajura'),
    ('Bajhang','Bajhang'),
    ('Achham','Achham'),
    ('Doti','Doti'),
    ('Kailali','Kailali'),
    ('Kanchanpur','Kanchanpur'),
    ('Dadeldhura','Dadeldhura'),
    ('Baitadi','Baitadi'),
    ('Darchula','Darchula'), 
)

# Create your models here.
class CustomUser(AbstractUser):
    user_type_data = (("1", "Owner"), ("2", 'Seller'), ("3", 'Customer'), ("4", "Delivery"))
    user_type = models.CharField(default = "1", choices = user_type_data, max_length = 10)
    email = models.EmailField(unique = True)
    
class Owner(models.Model):
    id = models.AutoField(primary_key = 1)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    def __str__(self):
        return self.admin.username

class Seller(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    number = models.BigIntegerField(null = True)
    Temporary_address = models.CharField(max_length = 300)
    street = models.CharField(max_length = 200)
    District = models.CharField(max_length = 50, choices = district, default = 'Kathmandu')
    profile_pic = models.ImageField(upload_to = "Seller_Profile", blank = True)
    gender = models.CharField(max_length = 100, choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    ), default = 'Male')
    KYC = models.ImageField(upload_to = 'KYC', blank = True)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
    def __str__(self):
        return self.admin.first_name

class Shop(models.Model):
    shop_owner = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    shop_name = models.CharField(max_length = 200)
    VAT = models.CharField(max_length = 300)
    address = models.CharField(max_length = 200)
    image = models.ImageField(upload_to ="shop_picture", blank=True)
    shop_number = models.BigIntegerField()
    objects = models.Manager()
    def __str__(self):
        return self.shop_name
    
class Customer(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    number = models.BigIntegerField(null=True)
    Temporary_address = models.CharField(max_length = 300)
    street = models.CharField(max_length = 200)
    District = models.CharField(max_length = 50)
    profile_pic = models.ImageField(upload_to = "Customer_Profile", blank = True)
    gender = models.CharField(max_length = 100, choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    ))
    objects = models.Manager()
    def __str__(self):
        return self.admin.email
    
class Service(models.Model):
    service_name = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=200, unique = True)
    image = models.ImageField(upload_to = 'services', blank = True)
    objects = models.Manager()
    class Meta:
        ordering = ('service_name',)
        verbose_name = 'service'
        verbose_name_plural = 'services'
    def __str__(self):
        return self.service_name
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.service_name)
        super(Service, self).save(*args, **kwargs)
    
    # def get_absolute_url(self):
    #     return reverse("shop:product_list_by_services", kwargs={"pk": self.pk})
    
class Category(models.Model):
    name = models.CharField(max_length = 200, db_index = True) 
    slug = models.SlugField(max_length= 200, unique = True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE,)
    created_by = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    image = models.ImageField(upload_to = 'category', blank = True)
    objects = models.Manager()
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    
    # def get_absolute_url(self):
    #     return reverse("shop:product_list_by_category", args=[self.slug])
    
class Sub_Category(models.Model):
    sub_name = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=200, unique = True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    created_by = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    image = models.ImageField(upload_to = 'sub-category', blank = True)
    objects = models.Manager()
    class Meta:
        ordering = ('sub_name',)
        verbose_name = 'sub_category'
        verbose_name_plural = 'sub_categories'
        
    def __str__(self):
        return self.sub_name
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.sub_name)
        super(Sub_Category, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("shop:product_list_by_sub_category", args=[self.slug])
class Brand(models.Model):
    brand_name = models.CharField(max_length = 200)
    slug = models.SlugField(max_length=200, unique = True)
    objects = models.Manager()
    class Meta:
        ordering = ('brand_name',)
        verbose_name = 'sub_category'
        verbose_name_plural = 'sub_categories'
        
    def __str__(self):
        return self.brand_name
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.brand_name)
        super(Brand, self).save(*args, **kwargs)
    

class Product(models.Model):   
    
    category = models.ForeignKey(Category, related_name= 'products', on_delete= models.CASCADE)
    sub_category = models.ForeignKey(Sub_Category, related_name='sub_category', on_delete=models.CASCADE, null = True)
    name = models.CharField(max_length = 200, db_index = True)
    service = models.ForeignKey(Service, related_name = 'product_service', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, db_index= True)
    short = models.CharField(max_length = 400, null= True,blank = True)
    commision = models.IntegerField(null = True, blank = True)
    discount = models.IntegerField(null = True, blank = True)
    image = models.ImageField(upload_to = 'products/%Y/%m/%d', blank = True)
    description = RichTextUploadingField()
    size = models.CharField(max_length = 100, default = "X, SM, L")
    price = models.DecimalField(max_digits= 20, decimal_places = 2)
    available_quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add= True)
    added_by = models.ForeignKey(CustomUser, related_name = 'added_by_user', on_delete=models.CASCADE)
    available = models.BooleanField(default= True)
    tags = TaggableManager()
    cashpayment = models.BooleanField(default=False)
    features = models.BooleanField(default=False)
    sale = models.CharField(max_length = 200, choices = (
        ('HotSale', 'Hot Sale'),
        ('FlashSale', 'Flash Sale'),
        ('ExclusiveSale', 'Exclusive Sale'),
        ('Normal', 'Normal')
    ), default = 'Normal')
    sponsor = models.BooleanField(default=False)
    allovernepal = models.BooleanField(default=False)
    from_shop = models.ForeignKey(Shop, related_name = 'fromshop', on_delete=models.CASCADE)
    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("shop:productDetails", args=[self.slug, self.id])

class imageList(models.Model):
    product_id = models.ForeignKey(Product, related_name = 'product_image', on_delete=models.CASCADE)
    image = models.ImageField(blank = True, upload_to = 'product_extra')
    
    def __str__(self):
        return self.product_id.name
        
class Delivery(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    fullname = models.CharField(max_length = 300)
    country = models.CharField(max_length = 60, default = 'Nepal')  
    number = models.BigIntegerField(null = True)
    district = models.CharField(max_length = 100,  default = 'Kathmandu')
    province = models.CharField(max_length = 200, null = True)
    ward_no = models.IntegerField()
    street = models.CharField(max_length = 200)
    profile_pic = models.ImageField(upload_to = "Vendor_Profile", blank = True)
    gender = models.CharField(max_length = 100, choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    ), default = 'Male')
    DOB = models.DateField(null = True)
    vechile_no = models.CharField(max_length = 200)
    vechile_color = models.CharField(max_length = 200)
    vechile_name = models.CharField(max_length = 200)
    license_no = models.CharField(max_length = 400)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add=True)
    permanent_country = models.CharField(max_length = 200, null = True)
    permanent_district = models.CharField(max_length = 200, null = True)
    permanent_address = models.CharField(max_length = 200, null = True)
    permanent_muncipalicity = models.CharField(max_length = 200, null = True)
    permanent_ward = models.CharField(max_length = 200, null = True)
    permanent_tole = models.CharField(max_length = 200, null = True)
    objects = models.Manager()
    
    def __str__(self):
        return self.fullname


class Delivery_address(models.Model):
    master = models.ForeignKey(Customer, related_name='deliveryaddress', on_delete=models.PROTECT)
    fullname = models.CharField(max_length = 200)
    number = models.BigIntegerField(null = True)
    region = models.CharField(max_length = 30)
    city = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    Area = models.CharField(max_length = 100)
    objects = models.Manager()

class totalVisit(models.Model):
    ip = models.GenericIPAddressField()
    

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == "1":
            Owner.objects.create(admin = instance)
        if instance.user_type == "2":
            Seller.objects.create(admin = instance)
        if instance.user_type == "3":
            Customer.objects.create(admin = instance)
        if instance.user_type == "4":
            Delivery.objects.create(admin = instance)

@receiver(post_save, sender=CustomUser)
def _post_save_receiver(sender, instance, **kwargs):
    if instance.user_type == "1":
        instance.owner.save()
    if instance.user_type == "2":
        instance.seller.save()
    if instance.user_type == "3":
        instance.customer.save()
    if instance.user_type == "4":
        instance.delivery.save()

    