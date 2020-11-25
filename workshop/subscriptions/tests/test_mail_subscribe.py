from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r

# Teste email content
class SubscribePostValid(TestCase):

    def setUp(self):
        post_example = dict(
            zip(
                ('name', 'cpf', 'email', 'phone'),
                ('John Doe', '12345678901', 'john@email.com', '(61)99999-9999')
            )
        )
        self.resp = self.client.post(r('inscricao'), post_example)
        self.email = mail.outbox[0]

    def test_subscription_subject_email(self):
        """Must return a standard subject"""
        expected = 'Formulário preenchido com sucesso'
        self.assertEqual(expected, self.email.subject)

    def test_subscription_from_email(self):
        """Must return the email sender"""
        expected = 'sender@email.com'
        self.assertEqual(expected, self.email.from_email)

    def test_subscription_email_to(self):
        """Must return the email to"""
        expected = ['sender@email.com', 'john@email.com']
        self.assertEqual(expected, self.email.to)

    def test_subscription_email_message(self):
        """Must return the email message with subscriber data"""
        contents = ('John Doe', '12345678901', 'john@email.com', '(61)99999-9999')

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
