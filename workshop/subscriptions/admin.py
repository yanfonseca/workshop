from django.contrib import admin
from workshop.subscriptions.models import Subscription

# Show model Subscription in /admin
admin.site.register(Subscription)