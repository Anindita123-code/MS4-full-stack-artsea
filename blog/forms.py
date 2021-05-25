from django import forms
from .models import Blog, CommentOnBlog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'blog_name': 'Short name for blog',
            'blog_title': 'Blog title for display',
            'blog_author': 'Author',
            'blog_content': 'Blog Paragraph 1',
            'blog_content_para2': 'Blog Paragraph 2 (Optional)',
            'blog_content_para3': 'Blog Paragraph 3 (Optional)',
        }
        self.fields['blog_content'].label = 'Blog Content - Primary'
        self.fields['blog_content_para2'].label = 'Blog Content - Second Paragraph'
        self.fields['blog_content_para3'].label = 'Blog Content - Third Paragraph'

        self.fields['blog_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'

          

class CommentOnBlogForm(forms.ModelForm):
    class Meta:
        model = CommentOnBlog
        fields =(
                    'comments',
                    'username',
                    'email',
                )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'comments': 'Post a comment on this blog',
            'username': 'Your name',
            'email': 'your email',
        }
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0'
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
