from django.contrib import admin
from .models import Lead, Profile
# Register your models here.

# admin.site.register(Profile)

class LeadAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'status', 'created_at')

    def full_name(self, obj):
        return obj.full_name
    full_name.short_description = 'Full Name'

admin.site.register(Lead, LeadAdmin)
