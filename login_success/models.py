from datetime import date
from django.db import models

# Create your models here.


class LoginMessages(models.Model):
    class Meta: verbose_name_plural = "Login Messages"

    message_date = models.DateField(date.today, default=date.today)
    message_title = models.CharField(max_length=254, null=True, blank=True)
    message_content =models.TextField(max_length=2000, null=True, blank=True)
    messages_visible = models.BooleanField(default=True)
    
    
    