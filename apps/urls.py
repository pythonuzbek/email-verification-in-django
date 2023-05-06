from django.urls import path

from apps.views import index_view, detail_view, add_product

urlpatterns = [
    path('', index_view, name='index_view'),
    path('detail/<uuid:id>/',detail_view, name='my_model_detail'),
    path('add-product',add_product,name='add_product')
]
