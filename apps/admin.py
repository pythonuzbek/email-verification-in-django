import csv

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin.options import InlineModelAdmin
from django.http import HttpResponse
from mptt.admin import DraggableMPTTAdmin
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from apps.models import Category, Product, ProductImage, Tag


@admin.register(Category)
class CategoryModelAdmin(DraggableMPTTAdmin):
    list_per_page = 5


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    fields = ('image',)
    min_num = 1
    extra = 1
    max_num = 5


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response




#
# class TagSelectWidget(FilteredSelectMultiple):
#     def __init__(self, *args, **kwargs):
#         super(TagSelectWidget, self).__init__(*args, **kwargs)
#         self.attrs['class'] = 'selectfilter'
#
# class ProductAdminForm(forms.ModelForm):
#     tags = forms.ModelMultipleChoiceField(
#         queryset=Tag.objects.all(),
#         widget=TagSelectWidget('Tag', is_stacked=False)
#     )
#
#     class Meta:
#         model = Product
#         fields = '__all__'


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    # form = ProductAdminForm
    inlines = [ProductImageInline]
    raw_id_fields = ['category']
    # exclude = ('tag',)


@admin.register(Tag)
class TagModelAdmin(ModelAdmin):
    pass
