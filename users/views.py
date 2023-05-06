from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import TemplateView

from shared.decorators import anonymous_required
from users.forms import RegisterForm, LoginForm
from users.models import User
from users.send_to_email import send_email
from users.token import account_activation_token


@anonymous_required(redirect_url='/')
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.data.get('email')
            password = form.data.get('password')
            user_ = User.objects.filter(email=email).first()
            user = authenticate(email=email, password=password)
            if user_ and not user_.is_active:
                messages.add_message(request,
                                     level=messages.WARNING,
                                     message='user is not active'
                                     )
            elif user:
                login(request, user)
            else:
                messages.add_message(request,
                                     level=messages.ERROR,
                                     message='email or password wrong'
                                     )
                return render(request, 'auth/login.html')
            return redirect('index_view')
    return render(request, 'auth/login.html')


@anonymous_required(redirect_url='/')
def register_view(request):
    context = {}
    if request.method == 'POST':
        forms = RegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            send_email(request, forms.data.get('email'), type_='register')
            return redirect('login_view')
        else:
            context['errors'] = forms.errors
    return render(request, 'auth/register.html', context)


def forgot_view(request):
    if request.method == 'POST':
        data = request.POST
        if User.objects.filter(email=data['email']).exists():
            send_email(request, data['email'], type_='forgot')
        else:
            messages.add_message(
                request,
                level=messages.ERROR,
                message='this email did not registered'
            )
    return render(request, 'auth/forgot-password.html')


def register_activate_email(request, uid, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid))
        user = User.objects.get(pk=uid)
    except Exception as e:
        print(e)
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login_view')
    else:
        return HttpResponse('Activate link is expired')


def forgot_activate_email(request, uid, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid))
        user = User.objects.get(pk=uid)
    except Exception as e:
        print(e)
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('reset_password')
    else:
        return HttpResponse('Activate link is expired')


def reset_password(request):
    return render(request, 'auth/reset-password.html')
