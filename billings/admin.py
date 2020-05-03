from django.contrib import admin

from billings.models.billing import Billing
from billings.models.order import Order

admin.site.register(Order)
admin.site.register(Billing)
