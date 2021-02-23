from django.contrib import admin
from .models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email' , 'phone' , 'comment_date')
    list_display_links = ('name',)
    search_fields = ('name' , 'email' , 'listing')
    list_per_page = 10

admin.site.register(Comment , CommentAdmin)