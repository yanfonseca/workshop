from django.apps import AppConfig

# Necessary change settings.py in installed apps:
# workshop.subscriptions to workshop.subscriptions.apps.SubscriptionsConfig
class SubscriptionsConfig(AppConfig):
    name = 'workshop.subscriptions'
    verbose_name = 'Controle de inscritos'