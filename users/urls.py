from django.urls import path

from users.views import login_view, register_view, forgot_view

urlpatterns = [
    path('login', login_view, name='login_view'),
    path('register', register_view, name='register_view'),
    path('forgot', forgot_view, name='forgot_view')
]
