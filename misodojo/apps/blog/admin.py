from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    # fields display on change list
    list_display = ['title', 'summary']
    # fields to filter the change list with
    list_filter = ['published', 'created', 'modified']
    # fields to search in change list
    search_fields = ['title', 'summary', 'content']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True


admin.site.register(Post, PostAdmin)
