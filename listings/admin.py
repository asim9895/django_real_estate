from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title' , 'price' , 'realtor' )
    list_display_links = ('title',)
    list_filter = ('realtor',)
    search_fields = ('title' , 'price' , 'realtor' , 'city' , 'state', 'zipcode')
    list_per_page = 3

admin.site.register(Listing, ListingAdmin)



