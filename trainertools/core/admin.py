from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Client, TrainerProfile
# Register your models here.


class TrainerProfileInline(admin.StackedInline):
    model = TrainerProfile
    can_delete = False
    verbose_name_plural = 'Trainer Profile'
    fk_name = 'user'
    fields = ('manager',)

class UserAdmin(BaseUserAdmin):
    inlines = (TrainerProfileInline,)
    list_display = ('username', 'email', 'get_manager')
    
    def get_manager(self, obj):
        if hasattr(obj, 'profile') and obj.profile.manager:
            return obj.profile.manager.user.username
        return "-"
    get_manager.short_description = "Manager"

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Client)