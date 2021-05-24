from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import BlogForm
from django.contrib import messages


def blog_list(request): 
    return render(request, 'blog/blog_list.html')


def add_blog(request):
    if request.method == 'POST':
        form_data = {
                'blog_name': request.POST['blog_name'],
                'blog_title': request.POST['blog_title'],
                'blog_author': request.POST['blog_author'],
                'blog_content': request.POST['blog_content'],
            }
        blog_form = BlogForm(form_data)
    
        if blog_form.is_valid():
            blog_form.save()
            messages.success(request, 'New Blog content Added Successfully !')
            return redirect(reverse('add_blog'))
        else:
            messages.error(request, 'Failed to add Blog post. Please ensure that the form is valid')
        form = blog_form
    else:
        form = BlogForm()
   
    template = 'blog/add_blog.html'
   
    context = {
        'form': form,
    }

    return render(request, template, context)

    
