import datetime

from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import forms, CharField
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from users.models import User


class ArticleForm(forms.Form):
    content = CharField(widget=CKEditorWidget())


User.objects.filter(date_joined__gte=datetime.datetime.now(timezone.utc) - datetime.timedelta(hours=24))


@admin.register(User)
class UserModelAdmin(UserAdmin):
    list_display = ('email', 'is_active', 'last_send_24hours')
    ordering = ('id',)
    search_fields = ('email',)
    actions = ['send_message']
    list_per_page = 3

    def last_send_24hours(self, obj):
        return obj.is_active

    last_send_24hours.boolean = True
    last_send_24hours.short_description = 'Last send message 24 hours'

    def send_message(self, request, queryset):
        form = ArticleForm()
        if 'apply' in request.POST:
            # The user clicked submit on the intermediate form.
            # Perform our update action:
            # TODO: send mail
            print('send mail')
            # Redirect to our admin view after our update has
            # completed with a nice little info message saying
            # our models have been updated:
            self.message_user(request, "Send messages to users ({})".format(queryset.count()))
            return HttpResponseRedirect(request.get_full_path())

        return render(request, 'admin/send_admin_message.html', {'orders': queryset, 'form': form})

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("date_joined",)}),
    )
    readonly_fields = ("date_joined",)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
