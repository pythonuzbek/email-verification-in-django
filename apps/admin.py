from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from apps.models import Category


@admin.register(Category)
class CategoryModelAdmin(DraggableMPTTAdmin):
    pass
