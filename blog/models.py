from django.db import models


class Blog(models.Model):
    blog_name = models.CharField(max_length=200, null=False, blank=False)
    blog_title = models.CharField(max_length=200, null=False, blank=False)
    blog_author = models.CharField(max_length=200, null=False, blank=False)
    blog_content = models.TextField(null=False, blank=False)
    blog_content_para2 = models.TextField(null=True, blank=True)
    blog_content_para3 = models.TextField(null=True, blank=True)
    blog_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_name


class CommentOnBlog(models.Model):
    Blog = models.ForeignKey(Blog, null=False, blank=False,
                             on_delete=models.CASCADE)
    username = models.CharField(max_length=254, null=True, blank=True)
    email = models.CharField(max_length=254, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comments
