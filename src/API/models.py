from django.db import models

class URL(models.Model):
    long_url = models.TextField()
    base62_id = models.CharField(max_length=7)