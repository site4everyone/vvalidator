from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.TextField()
    amount = models.IntegerField()
    desc = models.TextField()
    status = models.BooleanField(default=False)
