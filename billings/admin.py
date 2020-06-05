from django.contrib import admin

from billings.models.billing import Billing
from billings.models.order import Order


class BillingsAdmin(admin.ModelAdmin):
    list_display = ('status', 'order_id')
    list_filter = ['status']
    search_fields = ['order']

    def order_id(self, obj):
        return obj.id


class OrderAdmin(admin.ModelAdmin):
    list_display = ('owner', 'books_ids', 'order_price')

    def books_ids(self, obj):
        return obj.books_ids()


admin.site.register(Order, OrderAdmin)
admin.site.register(Billing, BillingsAdmin)
