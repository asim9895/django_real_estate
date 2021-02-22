from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email' , 'contact_date' )
    list_display_links = ('name',)
    
    search_fields = ('name' , 'listing' , 'email')
    list_per_page = 3

admin.site.register(Contact, ContactAdmin)