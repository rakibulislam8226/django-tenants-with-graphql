from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_number', 'phone')
    readonly_fields = ('account_number',)
