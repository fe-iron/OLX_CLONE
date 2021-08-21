from django.contrib import admin
from .models import Product, Category, Brand, ProductImages
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'category', 'condition', 'price', 'created')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


admin.site.register(Brand)
admin.site.register(ProductImages)
