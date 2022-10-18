from django.contrib import admin
from .models import PostModel, CommentModel, ContactModel
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'post_summery']
    search_fields = ['post_title']
    

admin.site.register(PostModel,PostModelAdmin)

class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['owner', 'post', 'comment_body', 'added_at']
    search_fields = ['owner']

admin.site.register(CommentModel,CommentModelAdmin)

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['Name', 'email', 'phone_number', 'contact_body', 'added_at']

admin.site.register(ContactModel,ContactModelAdmin)
