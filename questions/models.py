from django.db import models


class Questions(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    description = models.TextField()
