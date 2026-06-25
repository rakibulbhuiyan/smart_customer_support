from django.db import models
from django.conf import settings


class Conversation(models.Model):

    STATUS_CHOICES = (
        ("open", "Open"),
        ("pending", "Pending"),
        ("closed", "Closed"),
    )
    customer_name = models.CharField(max_length=255)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="open")
    assigned_agent = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.customer_name


class Message(models.Model):

    conversation = models.ForeignKey(Conversation,on_delete=models.CASCADE,related_name="messages")
    sender = models.CharField(max_length=20)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["timestamp"]