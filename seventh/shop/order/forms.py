from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address')

    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Введите имя"}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control",
               "placeholder": "Введите фамилию"}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "form-control",
               "placeholder": "Адрес электронной почты"}))
    address = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control",
               "placeholder": "Адрес доставки"}))
