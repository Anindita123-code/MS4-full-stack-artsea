from django.shortcuts import render
from .forms import BlogForm


def blog_list(request): 
    return render(request, 'blog/blog_list.html')


def add_blog(request):
    form = BlogForm()
    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

    
