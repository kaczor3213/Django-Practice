from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.TextField(null=True)
# Create your models here.
