from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

from auth_app.models import UserProfile

class Event(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('cancelled', 'Cancelled'),
        ('complete', 'Complete'),
    )
    
    title = models.CharField(max_length=200)
    venue = models.TextField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    duration = models.IntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    participants = models.ManyToManyField(User, related_name='participants', blank=True, null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})


        