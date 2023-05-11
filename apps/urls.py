from django.urls import path

from apps.views import index_view, detail_view, add_product, delete_product

urlpatterns = [
    path('', index_view, name='index_view'),
    path('product/<uuid:id>', detail_view, name='product_detail'''),
    path('add-product', add_product, name='add_product'),
    path('delete-product/<uuid:id>',delete_product,name='delete_product')
]
