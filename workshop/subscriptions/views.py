from django.core import mail
from django.shortcuts import render, redirect
from workshop.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        context = {'form': SubscriptionForm()}
        subject = 'subject'
        message = 'mensagem'
        from_email = 'contato@workshop.com'
        to_email = 'john@teste.com'
        recipient_list = [from_email, to_email]
        mail.send_mail(
            subject, message,
            from_email, recipient_list)
        return redirect('/inscricao/', context)

    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)
