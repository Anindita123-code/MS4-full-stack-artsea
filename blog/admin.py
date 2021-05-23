from django.contrib import admin
from .models import Blog, CommentOnBlog

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'blog_title',
        'blog_author',
        'blog_content',
        'blog_date', 
    )
    ordering = ('-blog_date',)


class CommentOnBlogAdmin(admin.ModelAdmin):
    list_display = (
        'Blog',
        'user',
        'date',
        'comments',
    )
    ordering = ('Blog',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(CommentOnBlog, CommentOnBlogAdmin)