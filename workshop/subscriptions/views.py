from django.conf import settings
from django.contrib import messages
from django.core import mail

from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.shortcuts import resolve_url as r

from workshop.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        # Method is_valid() returns boolean and do full_clean() too if returns True
        # The use of full_clean() alone accepts invalid forms
        if form.is_valid():
            subject = 'Formulário preenchido com sucesso'
            body = render_to_string('subscriptions/subscription_email.txt', form.cleaned_data)
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = form.cleaned_data['email']
            recipient_list = [from_email, to_email]
            mail.send_mail(subject=subject, message=body,
                           from_email=from_email, recipient_list=recipient_list)
            messages.success(request, "Formulário enviado!")
            return redirect(r('inscricao'))

        else:
            context = {'form': form}
            return render(request, 'subscriptions/subscription_form.html', context)

    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)
