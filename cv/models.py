from django.db import models
from django.utils import timezone

class Qualification(models.Model):
    institution = models.CharField(max_length=200)
    text = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.institution
