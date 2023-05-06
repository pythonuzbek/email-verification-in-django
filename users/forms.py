from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, PasswordInput, Form

from users.models import User


class RegisterForm(ModelForm):
    confirm_password = CharField(widget=PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'email', 'password')

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError("Password do not match")
        return make_password(password)


class LoginForm(Form):
    def clean_password(self):
        email = self.data.get('email')
        password = self.data.get('password')
        user = User.objects.get(email=email)
        if not user or user.check_password(password):
            raise ValidationError("Password or Username Do Not Match")
        return password


class ResetPassword(Form):
    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Password Do Not Match')
        user = User.objects.get()