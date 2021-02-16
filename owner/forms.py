from django import forms
from shop.models import Seller, CustomUser, Owner
from django.core.exceptions import ValidationError

class SellerForm(forms.ModelForm):
    first_name = forms.CharField(label = 'First Name', widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(label = 'Last Name', widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    email = forms.EmailField(label = 'Email', max_length = 200, widget = forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Email'}))
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
    re_password = forms.CharField(label = 'Repeat Password', widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Repeat Password'}))
    class Meta:
       model = Seller 
       fields = ('first_name', 'last_name','email', 'password','re_password','Temporary_address', 'number', 'District', 'street', 'gender', 'KYC')
       labels = {
           'District': 'District',
           'Temporary_address': 'City',
           'street' : 'Street Address',
           'gender'    : 'Gender',
           'KYC'         : 'Scan copy of National Id',
           'number' :'Phone Number'
           
       }
       widgets = {
           'District': forms.Select(attrs={'class':'form-control', 'placeholder' : 'District'}),
           'Temporary_address': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'City'}),
           'street': forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Street Address'}),
            'gender': forms.Select(attrs={'class':'form-control'}),
            'KYC': forms.FileInput(attrs={'class':'form-control', 'placeholder' : 'National ID Card'}),
            'number': forms.NumberInput(attrs={'class':'form-control', 'placeholder' : 'Your Phone Number'}),
   }
       
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            match = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            # Unable to find a user, this is fine
            return email
        # A user was found with this as a username, raise an error.
        raise forms.ValidationError('This email address is already in use.')
    def clean_number(self):
        data = self.cleaned_data['number']
        d = str(data)
        if len(d) > 10 or len(d) < 10 :
            raise ValidationError("Number can not be less or more than 10 digits")
        if not d.startswith('98'):
            raise ValidationError("Nepali number should start with 98")
        return data
    def clean_password(self):
        data = self.cleaned_data['password']
        d = str(data)
        if len(d) < 6:
            raise ValidationError("Password must be greater than 6 digits")
        return data
    def clean_re_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('re_password')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError('Password Did not Match')
        return password2
    
class OwnerEditForm(forms.ModelForm):
    first_name = forms.CharField(label = 'First Name', widget = forms.TextInput(attrs={'class':'form-control p-0 border-0', 'placeholder':'First Name'}))
    last_name = forms.CharField(label = 'Last Name', widget = forms.TextInput(attrs={'class':'form-control p-0 border-0', 'placeholder':'Last Name'}))
    email = forms.EmailField(label = 'Email', max_length = 200, widget = forms.TextInput(attrs={'class':'form-control p-0 border-0', 'placeholder' : 'Email'}))
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs={'class':'form-control p-0 border-0', 'placeholder':'Password'}))
    re_password = forms.CharField(label = 'Repeat Password', widget = forms.PasswordInput(attrs={'class':'form-control p-0 border-0', 'placeholder':'Repeat Password'}))
    class Meta:
       model = Owner 
       fields = ('address',)
       labels = {
           'address': 'Address',   
       }
       widgets = {
           'address': forms.TextInput(attrs={'class':'form-control p-0 border-0', 'placeholder' : 'Address'}),
       }
   

