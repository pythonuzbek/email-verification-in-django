from django.urls import path

from apps.views import detail_view, index_view

urlpatterns = [
    path('', index_view, name='index_view'),
    path('detail', detail_view, name='detail_view')
]
