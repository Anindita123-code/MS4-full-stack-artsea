from django.shortcuts import render


def blog_list(request): 
    return render(request, 'blog/blog_list.html')


def add_blog(request):
    return render(request, 'blog/add_blog.html')
