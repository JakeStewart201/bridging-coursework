from django.db import models
from django.utils import timezone

class Qualification(models.Model):
    institution = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    text = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.institution

class Skill(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    importance = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Interest(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    importance = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateField()
    link = models.URLField()

    def __str__(self):
        return self.title

class Job(models.Model):
    employer = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    text = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.employer
