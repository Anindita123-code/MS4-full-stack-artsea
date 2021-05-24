from django import forms
from .models import Blog, CommentOnBlog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('blog_name', 'blog_title', 'blog_author', 'blog_content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'blog_name': 'Short name for blog',
            'blog_title': 'Blog title for display',
            'blog_author': 'Author',
            'blog_content': 'Blog Content',
        }

        self.fields['blog_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            self.fields[field].label = False


class CommentOnBlogForm(forms.ModelForm):
    class Meta:
        model = CommentOnBlog
        fields = ('comments',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
