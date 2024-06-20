from django.db import models
from datetime import date

# Create your models here.
class Review(models.Model):
    username = models.CharField(max_length=40)
    user_review = models.TextField()
    ratings = models.IntegerField()

class Memory(models.Model):
    username = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.FileField(upload_to="user_memories/",max_length=2500, null=True, default=None)
    about = models.TextField()
    date = models.DateField(default=date.today)