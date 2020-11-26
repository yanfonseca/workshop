from django.db import models

class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('E-mail')
    phone = models.CharField('Telefone', max_length=20)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    paid = models.BooleanField('pago',default=False)

    # Used to change standard options of Django's ORM
    class Meta:
        verbose_name_plural = 'Inscrições'
        verbose_name = 'Inscrição'

        # Make ordering ascend a standard
        ordering = ('-created_at', )

    # Used to show objects name in django admin
    def __str__(self):
        return self.name