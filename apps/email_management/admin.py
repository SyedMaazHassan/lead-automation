from django.contrib import admin
from .models import EmailTemplate, Email, ChatMessage
# Register your models here.

admin.site.register(EmailTemplate)
admin.site.register(Email)
admin.site.register(ChatMessage)