from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TODO(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length = 500, blank = True)
    creation_date = models.DateTimeField(auto_now_add = True)
    completion_date = models.DateTimeField(null = True, blank = True)
    important_check = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.title