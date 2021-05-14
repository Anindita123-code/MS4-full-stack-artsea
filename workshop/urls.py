from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_workshops, name='workshops'),
    path('<int:workshop_id>/', views.workshop_details, name='workshop_details'),
    path('add/', views.add_workshops, name='add_workshop'),
    path('edit/<int:workshop_id>', views.edit_workshop, name='edit_workshop'),
    
]