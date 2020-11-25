from django.conf import settings
from django.contrib import messages
from django.core import mail
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
            # from_email = 'sender@email.com'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = form.cleaned_data['email']
            recipient_list = [from_email, to_email]
            mail.send_mail(
                subject=subject, message=body,
                from_email=from_email, recipient_list=recipient_list)
            messages.success(request, "Formulário enviado!")
            return redirect('/inscricao/')

        else:
            context = {'form': form}
            return render(request, 'subscriptions/subscription_form.html', context)

    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)
