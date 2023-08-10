from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from account.models import User, ClientUser
from account.forms import CustomUserCreationForm


@admin.register(User)
class MyUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    fieldsets = (
        (_('Login Information'), {'fields': ('email', 'username', 'password')}),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'is_client', 'is_employee', 'groups', 'user_permissions'
            )
        }),
        (_('Dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # ADD USER FIELD
    add_fieldsets = (
        (_('Login Information'), {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'username', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('date_joined',)
    filter_horizontal = (
        'groups',
        'user_permissions',
    )

@admin.register(ClientUser)
class ClientUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('User'), {'fields': ('user',)}),
        (_('Personal Information'), {'fields': ('first_name', 'last_name', 'phone_number')}),
        # (_('Address'), {'fields': ('default_billing_address',)}),
        (_('Note'), {'fields': ('note',)})
    )

    list_display = ('user', 'first_name', 'last_name', 'phone_number')
    search_fields = ('user__email__icontains',)