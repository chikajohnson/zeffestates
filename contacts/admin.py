from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'contact_date')
    list_display_link = ('id', 'name')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 5


admin.site.register(Contact, ContactAdmin)

