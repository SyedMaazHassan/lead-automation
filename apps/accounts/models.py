from django.db import models
from django.contrib.auth.models import User


# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization_info = models.TextField(blank=True, null=True)
    payment_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Profile for {self.user.username}"


class Lead(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Cold Email sent', 'Cold Email sent'),
        ('Nurturing email sent', 'Nurturing email sent'),
        ('Closed', 'Closed'),
        ('Responded', 'Responded'),
        # Add other status choices as needed
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    background = models.TextField(null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.status}"
