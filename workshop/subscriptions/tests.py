from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r
from workshop.subscriptions.forms import SubscriptionForm


class SubscribeTestGet(TestCase):

    def setUp(self):
        self.resp = self.client.get(r('inscricao'))

    def test_get(self):
        """Get /cadastro/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must return subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_htmlpage(self):
        """Must contain input tags in the html"""

        html = (('<form', 1),
                ('<input', 6),
                ('type="text"', 3),
                ('type="submit"', 1),
                ('type="email"', 1))

        for tag, count in html:
            with self.subTest():
                self.assertContains(self.resp, tag, count)

    def test_csrf(self):
        """Must contain csrf in the html"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    # Conect html and form
    def test_has_form(self):
        """Context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_fields(self):
        """Form must have some fields"""
        form = self.resp.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))


class SubscribePostValid(TestCase):

    def setUp(self):
        post_example = dict(
            zip(
                ('name', 'cpf', 'email', 'phone'),
                ('John Doe', '12345678901', 'john@email.com', '(61)99999-9999')
            )
        )
        self.resp = self.client.post(r('inscricao'), post_example)

    def test_post(self):
        """Valid Post must redirect to /subscribe/"""
        self.assertEqual(302, self.resp.status_code)

    def test_send_subscribe(self):
        """Valid POST must send one email"""
        self.assertEqual(1, len(mail.outbox))

    def test_subscription_subject_email(self):
        """Must return a standard subject"""
        email = mail.outbox[0]
        expected = 'Formulário preenchido com sucesso'
        self.assertEqual(expected, email.subject)

    def test_subscription_from_email(self):
        """Must return the email sender"""
        email = mail.outbox[0]
        expected = 'sender@email.com'
        self.assertEqual(expected, email.from_email)

    def test_subscription_email_to(self):
        """Must return the email to"""
        email = mail.outbox[0]
        expected = ['sender@email.com', 'john@email.com']
        self.assertEqual(expected, email.to)

    def test_subscription_email_message(self):
        """Must return the email message with subscriber data"""
        email = mail.outbox[0]

        contents = ('John Doe', '12345678901', 'john@email.com', '(61)99999-9999')

        for content in contents:
            with self.subTest():
                self.assertIn(content, email.body)


class SubscribeInvalidPost(TestCase):

    def setUp(self):
        self.resp = self.client.post(r('inscricao'), {})

    def test_post(self):
        """Invalid POST must not redirect"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must return subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        """Must have a form as instance"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_erro(self):
        """Must have message errors"""
        form = self.resp.context['form']
        self.assertTrue(form.errors)


class SubscribeSucessMessage(TestCase):
    def test_message(self):
        """Should follow and show a message"""
        post_example = dict(
            zip(
                ('name', 'cpf', 'email', 'phone'),
                ('John Doe', '12345678901', 'john@email.com', '(61)99999-9999')
            )
        )

        # Follow set to True and returns status 200
        resp = self.client.post(r('inscricao'), post_example, follow=True)
        self.assertContains(resp, "Formulário enviado!")
