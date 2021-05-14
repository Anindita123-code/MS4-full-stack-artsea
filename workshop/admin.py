from django.contrib import admin
from .models import Workshop, Category

# Register your models here.
class WorkshopAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
        'workshop_name',
        'title', 
        'description',
        'hosted_by', 
        'date_and_time', 
        'venue', 
        'image_url', 
        'image',
    )
    ordering = ('workshop_name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    ordering = ('-name',)


admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Category, CategoryAdmin)

