from django.conf import settings
from django.contrib import messages
from django.core import mail

from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.shortcuts import resolve_url as r

from workshop.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        return create_subscription(request)

    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)

def create_subscription(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})

    # Params
    subject = 'Formulário preenchido com sucesso'
    template_name = 'subscriptions/subscription_email.txt'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = form.cleaned_data['email']
    context = form.cleaned_data

    # Send email
    _send_mail(subject, from_email, to_email, template_name, context)

    # Show success
    messages.success(request, "Formulário enviado!")

    return redirect(r('inscricao'))


def _send_mail(subject, from_email, to_email, template_name, context):
    body = render_to_string(template_name,
                            context)
    mail.send_mail(subject,
                   body, from_email,
                   [from_email, to_email])

# Obs:
# Method is_valid() returns boolean and do full_clean() too if returns True
# The use of full_clean() alone accepts invalid forms
