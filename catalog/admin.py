from django.contrib import admin
from .models import Catalog
from .models import Order

# Register your models here.
admin.site.register(Catalog)



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'product', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'phone', 'product__name')