from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.TextField(null=True)
# Create your models here.

class Client(models.Model):
    secondname = models.CharField(max_length=50)
    age = models.IntegerField()
    country = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    programming_language = models.CharField(max_length=20)
    payment = models.CharField(max_length=50)
    
    def __str__(self):
        return self.secondname + self.age + self.country + self.email + self.programming_language + self.payment
    