from django.contrib import admin
from blog.models import Post


# Register your models here.


class Post_disp(admin.ModelAdmin):
    list_display = ('Title', 'short_body', 'created_by', 'status', 'publish')
    list_filter = ('Title', 'publish', 'status')
    search_fields = ('Title', 'Body')
    prepopulated_fields = {'slug': ('Title',)}

admin.site.register(Post, Post_disp)
