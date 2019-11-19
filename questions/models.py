from djongo import models


class Questions(models.Model):
    name = models.TextField()
    tagline = models.CharField(max_length=200)
    description = models.TextField()
