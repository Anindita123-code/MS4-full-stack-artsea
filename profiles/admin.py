from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):

    fields = ('user', 'default_phone_number', 'default_country',
              'default_town_or_city')

    list_display = ('user', 'default_phone_number', 'default_country',
              'default_town_or_city',)


admin.site.register(UserProfile, UserProfileAdmin)