from django.shortcuts import render, redirect
from workshop.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        context = {'form': SubscriptionForm()}
        return redirect('/inscricao/', context)

    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)
