from django.db import models


# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver

EMAIL_TYPE_CHOICES = [
    ('Introductory Email', 'Introductory Email'),
    ('Product Announcement', 'Product Announcement'),
    ('Cold Email', 'Cold Email'),
    ('Follow up', 'Follow up'),
    ('Survey Request', 'Survey Request'),
    ('Special Offer', 'Special Offer'),
    # Add other type choices as needed
]

# Create your models here.
class EmailTemplate(models.Model):
    name = models.CharField(max_length=255)
    template_type = models.CharField(max_length=255, choices=EMAIL_TYPE_CHOICES)
    email_subject = models.CharField(max_length=255)
    email_body = models.TextField()
    profile = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Email(models.Model):
    email_type = models.CharField(max_length=255, choices=EMAIL_TYPE_CHOICES)
    sent_to_lead = models.ForeignKey('accounts.Lead', on_delete=models.CASCADE, related_name="sent_email")
    template = models.ForeignKey('email_management.EmailTemplate', on_delete=models.CASCADE)
    email_subject = models.CharField(max_length=255)
    email_body = models.TextField()
    is_sent = models.BooleanField(default=False)
    profile = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email_type} to {self.sent_to_lead.first_name} {self.sent_to_lead.last_name}"


class ChatMessage(models.Model):
    SENDER_CHOICES = [
        ('user', 'User'),
        ('ai', 'AI'),
    ]
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)
    created_template = models.OneToOneField('email_management.EmailTemplate', on_delete=models.SET_NULL, null=True, blank=True)
    lead = models.ForeignKey('accounts.Lead', on_delete=models.CASCADE)
    message = models.TextField()
    profile = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} - {self.message} ({self.created_at})"
