from django.contrib import admin
from django.urls import path

from workshop.subscriptions.views import subscribe

# app_name = 'subscriptions'

urlpatterns = [
    path('', subscribe, name='inscricao'),
]