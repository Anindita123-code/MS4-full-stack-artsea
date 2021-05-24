from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    blog_name = models.CharField(max_length=200, null=False, blank=False)
    blog_title = models.CharField(max_length=200, null=False, blank=False)
    blog_author = models.CharField(max_length=200, null=False, blank=False)
    blog_content = models.TextField(null=False, blank=False)
    blog_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title


class CommentOnBlog(models.Model):
    Blog = models.ForeignKey(Blog, null=False, blank=False,
                             on_delete=models.CASCADE,
                             related_name='Blog_name')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comments = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.comments



