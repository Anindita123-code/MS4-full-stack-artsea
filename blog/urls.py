from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('add/', views.add_blog, name='add_blog'),
    path('<int:blog_id>/', views.show_blog, name='show_blog'),
    # path('comment/<int:blog_id>/', views.add_comments, name='add_comments'),

]