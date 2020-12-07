from django import forms
from django.core.exceptions import ValidationError


def validade_cpf(value):
    """Validates accepts only one value."""
    if not value.isdigit():
        raise ValidationError('CPF precisa ter apenas números', 'digits_cpf')

    if len(value) != 11:
        raise ValidationError('CPF precisa ter 11 números', 'lenght_cpf')

class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validade_cpf])
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Celular')

    # clean_ is a standard that django searches for, like test_ from unittest
    def clean_name(self):
        name = self.cleaned_data['name']
        capitalized_name = [w.capitalize() for w in name.split()]
        return ' '.join(capitalized_name)
