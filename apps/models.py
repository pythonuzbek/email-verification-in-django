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
    category = ForeignKey('apps.Category', CASCADE)
    author = ForeignKey('users.User', CASCADE)

    @property
    def discount_price(self):
        return self.price - self.price * self.discount // 100


class ProductImage(BaseIDModel):
    image = ImageField(upload_to='media/')
    product = ForeignKey('apps.Product', CASCADE,'images')

    def save(self, *args, **kwargs):
        if not self.pk:
            filename = self.product.id
            self.image.name = filename
        super().save(*args, **kwargs)


class Comment(BaseIDModel, BaseDateModel):
    product = ForeignKey('apps.Product', CASCADE)
    text = TextField(max_length=255)
    star = SmallIntegerField(default=0)
    author = ForeignKey('users.User', CASCADE)
