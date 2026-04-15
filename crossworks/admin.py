from django.contrib import admin
from .models import EnquiryForm


@admin.register(EnquiryForm)
class UserEntryAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'ph_no', )
    search_fields=('name',)