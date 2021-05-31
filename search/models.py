from django.db import models
from django.utils import timezone

class Search(models.Model):
    query = models.CharField(max_length=100)
    is_valid = models.BooleanField(default=False)
    search_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.query} - {'valid' if self.is_valid else 'invalid'}"