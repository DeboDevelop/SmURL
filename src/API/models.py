from django.db import models

class URL(models.Model):
    long_url = models.URLField("URL", unique=True)
    base62_id = models.CharField(max_length=7)