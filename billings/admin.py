from django.contrib import admin

from billings.models import Order, Billing

admin.site.register(Order)
admin.site.register(Billing)
