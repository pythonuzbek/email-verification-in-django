from ckeditor.fields import RichTextField
from django.db.models import (CASCADE, CharField, ForeignKey, ImageField,
                              Model, PositiveIntegerField, SmallIntegerField,
                              TextField, TextChoices, ManyToManyField)
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from shared.models import BaseDateModel, BaseIDModel, upload_name


class Category(MPTTModel, BaseIDModel):
    name = CharField(max_length=255)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(BaseIDModel):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(BaseIDModel,BaseDateModel):
    name = CharField(max_length=255)
    price = PositiveIntegerField()
    discount = SmallIntegerField(default=0)
    detail = RichTextField()
    quantity = PositiveIntegerField(default=0)
    category = ForeignKey('apps.Category', CASCADE)
    tag = ManyToManyField('apps.Tag','tags',null=True,blank=True)
    author = ForeignKey('users.User', CASCADE)

    def __str__(self):
        return self.name

    @property
    def discount_price(self):
        return self.price - self.price * self.discount // 100


class ProductImage(BaseIDModel):
    class Type(TextChoices):
        IMAGES = 'images', 'Rasmlar'
        DOCUMENTS = 'documents', 'Dokumentlar'
        VIDEOS = 'videos', 'Videolar'

    image = ImageField(upload_to=upload_name)
    product = ForeignKey('apps.Product', CASCADE,'images')
    type = CharField(max_length=15, choices=Type.choices)


class Comment(BaseIDModel, BaseDateModel):
    product = ForeignKey('apps.Product', CASCADE)
    text = TextField(max_length=255)
    star = SmallIntegerField(default=0)
    author = ForeignKey('users.User', CASCADE)
