from django.core import mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from workshop.subscriptions.forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        post_example = dict(
            zip(
                ('name', 'cpf', 'email', 'phone'),
                ('John Doe', '12345678901', 'john@email.com', '(61)99999-9999')
            )
        )

        context = {'form': SubscriptionForm()}

        subject = 'Formulário preenchido com sucesso'
        body = render_to_string('subscriptions/subscription_email.txt', post_example)
        from_email = 'sender@email.com'
        to_email = 'john@email.com'
        recipient_list = [from_email, to_email]
        mail.send_mail(
            subject, body,
            from_email, recipient_list)
        return redirect('/inscricao/', context)

    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)

