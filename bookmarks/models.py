from django.db import models

# Create your models here.

class Bookmark(models.Model):
    title = models.CharField(max_length=40, blank=True, null=True)
    url = models.URLField('url', unique=True)
