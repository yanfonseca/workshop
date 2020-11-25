from django.core import mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from workshop.subscriptions.forms import SubscriptionForm


def subscribe(request):

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            # form.full_clean()
            subject = 'Formulário preenchido com sucesso'
            body = render_to_string('subscriptions/subscription_email.txt', form.cleaned_data)
            from_email = 'sender@email.com'
            to_email = form.cleaned_data['email']
            recipient_list = [from_email, to_email]
            mail.send_mail(
                subject, body,
                from_email, recipient_list)
            return redirect('/inscricao/')

        else:
            context = {'form': form}
            return render(request, 'subscriptions/subscription_form.html', context)

    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)
