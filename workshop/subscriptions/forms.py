from django import forms
from django.core.exceptions import ValidationError


def validate_cpf(value):
    """Validates accepts only one value."""
    if not value.isdigit():
        raise ValidationError('CPF precisa ter apenas números', 'digits_cpf')

    if len(value) != 11:
        raise ValidationError('CPF precisa ter 11 números', 'lenght_cpf')

class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(label='Celular', required=False)

    # clean_ is a standard that django searches for, like test_ from unittest
    # Modify field name, clean_name
    def clean_name(self):
        name = self.cleaned_data['name'] # Old cleaned_data
        capitalized_name = [w.capitalize() for w in name.split()]
        return ' '.join(capitalized_name)

    # form's clean, to analyse two fields at the same time
    def clean(self):
        if (not self.cleaned_data.get('email') and not self.cleaned_data.get('phone')): # Must use get to avoid error with dictionary key.
            raise ValidationError('Por favor, informe seu e-mail ou telefone.')

        return self.cleaned_data