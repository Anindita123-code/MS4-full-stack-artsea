from django.contrib import admin
from .models import Blog, CommentOnBlog

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'blog_name',
        'blog_title',
        'blog_author',
        'blog_content',
        'blog_content_para2',
        'blog_content_para3',
        'blog_date',
    )
    ordering = ('-blog_date',)


class CommentOnBlogAdmin(admin.ModelAdmin):
    list_display = (
        # 'blog_id',
        'date',
        'comments',
        'username',
        'email',
    )
    ordering = ('-date',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(CommentOnBlog, CommentOnBlogAdmin)
