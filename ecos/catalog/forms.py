from django import forms


class CustomerForm(forms.Form):
    phone = forms.CharField(label="Ваш номер телефона")
    name = forms.CharField(required=False, label="Ваше имя")
    address = forms.CharField(required=False, label="Адрес доставки")