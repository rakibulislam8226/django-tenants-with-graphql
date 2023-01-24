from django.contrib import admin

# Register your models here.
from .models import SweetType

@admin.register(SweetType)
class SweetTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)