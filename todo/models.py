from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    created_at = models.DateField(auto_now=True)