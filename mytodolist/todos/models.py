# todos/models.py
from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    # ... any other fields ...

    def __str__(self):
        return self.title
