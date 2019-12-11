from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from material import *
from cashReg.models import AddProduct


class SignUpForm(UserCreationForm):
    username = forms.CharField()
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(label="Email Address")
    password1 = forms.CharField(widget=forms.PasswordInput, label="Enter password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm password")
    receive_news = forms.BooleanField(required=False, label='I want to receive news and notifications')
    agree_toc = forms.BooleanField(required=True, label='I agree with the Terms and Conditions')

    layout = Layout('username', 'email',
                    Row('password1', 'password2'),
                    Fieldset('Personal details',
                             Row('first_name', 'last_name'),
                             'receive_news', 'agree_toc'))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class AddProductForm(forms.ModelForm):
    Category_Name = forms.CharField()
    Product_Name = forms.CharField()
    Quantity = forms.IntegerField()
    Price = forms.FloatField()

    layout = Layout(Fieldset('Product details',
                             Row('Category_Name', ),
                             Row('Product_Name', 'Quantity'),
                             Row('Price'), ))

    class Meta:
        model = AddProduct
        fields = ('Product_Name', 'Category_Name', 'Quantity', 'Price')
