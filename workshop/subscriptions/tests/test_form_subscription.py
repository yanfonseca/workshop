from django.test import TestCase
from workshop.subscriptions.forms import SubscriptionForm


# Test object form
class SubscriptionFormTest(TestCase):

    def test_form_has_fields(self):
        """Form must have some fields"""
        form = SubscriptionForm()
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))

    def test_cpf_is_digit(self):
        """"CPF must be digits"""
        form = self.make_validated_form(cpf='ABCD5678901')
        # self.assertListEqual(['cpf'], list(form.errors))
        # msg = 'CPF precisa ter apenas números'
        # field ='cpf'
        # self.assertFormErrorMessage(form, field, msg)
        msg = 'CPF precisa ter apenas números'
        field ='cpf'
        code ='digits_cpf'
        self.assertFormErrorCode(form, field, code)

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits"""
        form = self.make_validated_form(cpf='5678901')
        #self.assertListEqual(['cpf'], list(form.errors))
        # msg = 'CPF precisa ter 11 números'
        # field = 'cpf'
        # self.assertFormErrorMessage(form, field, msg)
        field = 'cpf'
        code = 'lenght_cpf'
        self.assertFormErrorCode(form, field, code)

    def test_name_must_be_capitalized(self):
        """Name must be capitalized"""
        # JOHN doe -> John Doe
        form = self.make_validated_form(name='JOHN doe')
        self.assertEqual('John Doe', form.cleaned_data['name'])

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    # def assertFormErrorMessage(self, form, field, msg):
    #     errors = form.errors
    #     errors_list = errors[field]
    #     self.assertListEqual([msg], errors_list)


    def make_validated_form(self, **kwargs):
        valid_example = dict(
            zip(
                ('name', 'cpf', 'email', 'phone'),
                ('John Doe', '12345678901', 'john@email.com', '(61)99999-9999')
            )
        )
        data_example = dict(valid_example, **kwargs)
        form = SubscriptionForm(data_example)
        form.is_valid()
        return form
# If you want to test form from the page

# from django.test import TestCase
# from django.shortcuts import resolve_url as r
#
# class SubscriptionFormTest(TestCase):
#
#     def setUp(self):
#         self.resp = self.client.get(r('inscricao'))
#
#     def test_form_has_fields(self):
#         """Form must have some fields"""
#         form = self.resp.context['form']
#         self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))
