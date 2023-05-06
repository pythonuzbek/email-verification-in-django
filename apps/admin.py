from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from mptt.admin import DraggableMPTTAdmin

from apps.models import Category, Product, ProductImage


@admin.register(Category)
class CategoryModelAdmin(DraggableMPTTAdmin):
    pass


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    fields = ('image',)
    min_num = 1
    extra = 1
    max_num = 5


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
