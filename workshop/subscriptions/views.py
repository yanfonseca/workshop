from django.core import mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from workshop.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        context = {'form': SubscriptionForm()}

        subject = 'Formulário preenchido com sucesso'
        body = MENSAGEM #render_to_string('subscriptions/subscription_email.txt')
        from_email = 'sender@email.com'
        to_email = 'john@email.com'
        recipient_list = [from_email, to_email]
        mail.send_mail(
            subject, body,
            from_email, recipient_list)
        return redirect('/inscricao/', context)

    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)

MENSAGEM = """
Olá!

Bem vindo ao melhor workshop do mundo!

Os dados informados foram:
nome: John Doe
cpf: 12345678901
Email: john@email.com
Telefone: (61)99999-9999
"""
