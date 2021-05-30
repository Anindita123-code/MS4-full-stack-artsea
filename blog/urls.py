from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('add/', views.add_blog, name='add_blog'),
    path('<int:blog_id>/', views.show_blog, name='show_blog'),
    path('edit/<int:blog_id>', views.edit_blog, name='edit_blog'),
    path('delete/<int:blog_id>', views.delete_blog, name='delete_blog'),
]
