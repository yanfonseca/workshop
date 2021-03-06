from django.contrib import admin
from django.utils.timezone import now
from workshop.subscriptions.models import Subscription

# Register the model Subscription in /admin, a standard apresentation in the django admin
#admin.site.register(Subscription)

class SubscriptionModelAdmin(admin.ModelAdmin):

    # Add a display columns names in /admin
    list_display = ('name', 'email',
                    'phone', 'cpf',
                    'created_at', 'subscribed_today', 'paid')

    # Add a hierarchy ordenation for the column
    date_hierarchy = 'created_at'

    # Add a search field with a order to search
    search_fields = ('name', 'email', 'phone', 'cpf', 'created_at')

    # Add a filter to facilitate the user's navigation
    list_filter = ('created_at','paid')

    # Actions
    actions = ['mark_as_paid']

    # Add a column with True/False values
    def subscribed_today(self, obj):
        return obj.created_at.day == now().day

    # Change the column name 'subscribed_today' to 'Inscrito hoje'
    subscribed_today.short_description = 'Inscrito hoje'

    # If want to a graphic marker uncomment the line above
    #subscribed_today.boolean = True

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)

        if count == 1:
            msg = '{} inscrição foi marcada como paga.'
        else:
            msg = '{} inscrições foram marcada como pagas.'

        self.message_user(request, msg.format(count))

    mark_as_paid.short_description = 'Marcar como pago'


# Register the model Subscription in /admin and accepts alterations in the apresentation in the django admin
admin.site.register(Subscription, SubscriptionModelAdmin)


