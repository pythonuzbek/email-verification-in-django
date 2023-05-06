from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import login_view, register_view, forgot_view, \
    register_activate_email, forgot_activate_email, reset_password

urlpatterns = [
    path('login', login_view, name='login_view'),
    path('register', register_view, name='register_view'),
    path('logout', LogoutView.as_view(
        next_page='/'
    ), name='logout'),
    path('forgot', forgot_view, name='forgot_view'),

    path('activate-register/<str:uid>/<str:token>',register_activate_email),
    path('activate-forgot/<str:uid>/<str:token>',forgot_activate_email),
    path('reset-password',reset_password,name='reset_password')
]
