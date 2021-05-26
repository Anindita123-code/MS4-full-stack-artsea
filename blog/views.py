from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import BlogForm, CommentOnBlogForm
from .models import Blog, CommentOnBlog
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required


def blog_list(request): 
    blogs = Blog.objects.all()
    template = 'blog/blog_list.html'

    context = {
        'blog_list': blogs,
    }

    return render(request, template, context)


def show_blog(request, blog_id):
    single_blog = get_object_or_404(Blog, pk=blog_id)
    blog_comments = CommentOnBlog.objects.all()
    comments_on_blog = blog_comments.filter(Blog_id__id__in=(blog_id,))
    
    form = CommentOnBlogForm()
    template = 'blog/blog_detail.html'
    if request.method == "POST":

        form_data = {
                    'comments': request.POST['comments'],
                }

        form = CommentOnBlogForm(form_data)
       
        if form.is_valid():
            comment = form.save(commit=False)
            comment.Blog_id = blog_id
            comment.username = request.POST['username']
            comment.email = request.POST['email']
            comment.save()
            messages.success(request, 'New Blog content Added Successfully !')
            return redirect(reverse('show_blog', args=(blog_id,)))
        else:
            messages.error(request, 'Failed to add comment to the Blog post. Please ensure that the form is valid')

    context = {
        'blog': single_blog,
        'form': form,
        'comments_on_blog': comments_on_blog,
    }
    return render(request, template, context)


@login_required
def add_blog(request):
    if request.method == 'POST':
        form_data = {
                'blog_name': request.POST['blog_name'],
                'blog_title': request.POST['blog_title'],
                'blog_author': request.POST['blog_author'],
                'blog_content': request.POST['blog_content'],
                'blog_content_para2': request.POST['blog_content_para2'],
                'blog_content_para3': request.POST['blog_content_para3'],
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


@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Blog!')
            return redirect(reverse('show_blog', args=(blog_id,)))
        else:
            messages.error(request, 'Failed to update Blog. Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)
    
    messages.info(request, f'You are editing {blog.blog_title}')
    template = 'blog/edit_blog.html'
    
    context = {
        'form': form,
        'blog': blog,
    }
    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry! Only Administrator can do that')
        return redirect(reverse('home'))
        
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, 'Blog Deleted!')

    return redirect(reverse('blog_list'))
    
