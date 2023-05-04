from ckeditor.fields import RichTextField
from django.db.models import CharField, Model, CASCADE, ForeignKey, PositiveIntegerField, ImageField, TextField, \
    SmallIntegerField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from shared.models import BaseIDModel, BaseDateModel, upload_name


class Category(MPTTModel, BaseIDModel):
    name = CharField(max_length=255)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ('name',)


class Product(BaseIDModel, BaseDateModel):
    name = CharField(max_length=255)
    price = PositiveIntegerField()
    discount = SmallIntegerField(default=0)
    detail = RichTextField()
    quantity = PositiveIntegerField(default=0)


class ProductImage(BaseIDModel):
    image = ImageField(upload_to=upload_name)
    product = ForeignKey('apps.Product', CASCADE)


class Comment(BaseIDModel, BaseDateModel):
    product = ForeignKey('apps.Product', CASCADE)
    text = TextField(max_length=255)
    star = SmallIntegerField(default=0)
    author = ForeignKey('users.User', CASCADE)
