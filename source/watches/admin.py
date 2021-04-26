from django.contrib import admin

from .models import Product, Order, ProductOrder

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'category', 'product_availability', 'price']
    list_filter = ['category']
    search_fields = ['name']
    fields = ['name', 'description', 'category', 'product_availability', 'price']

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(ProductOrder)
