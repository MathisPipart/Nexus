from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'url', 'role')
    list_filter = ('user',)
    search_fields = ('user__username', 'user__email')

# admin.site.register(UserProfile, UserProfileAdmin)
