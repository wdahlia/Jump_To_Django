from subprocess import CompletedProcess
from django.db import models

# Create your models here.

class Todo(models.Model):
    content = models.CharField(max_length=80)
    completed = models.BooleanField(default=False)
    priority = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    deadline = models.DateField(null=True)
    
