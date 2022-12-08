from django import forms


class CustomerForm(forms.Form):
    phone = forms.IntegerField(min_value=99999999, label="Ваш номер телефона")
    name = forms.CharField(required=False, label="Ваше имя")
    address = forms.CharField(required=False, label="Адрес доставки")