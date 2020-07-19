from django.db import models

class URL(models.Model):
    """
    This the URL Modle class, this class defines the table URL to store the long url in database and the base62 token.
    """
    long_url = models.URLField("URL", unique=True)
    base62_id = models.CharField(max_length=7, unique=True)