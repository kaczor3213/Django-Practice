from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=31, unique=True)

    def __str__(self):
        return self.name

class Payment(models.Model):
    payment_type = models.CharField(max_length=31, unique=True)

    def __str__(self):
        return self.name
    
class Country(models.Model):
    name = models.CharField("Country", max_length=31, unique=True)
    code = models.CharField("Iso Code", max_length=3, unique=True)
    
    class Meta:
        ordering = ['name']
        unique_together = ['name', 'code']
        get_latest_by = 'name'
    
    def __str__(self):
        return self.name + self.code

class Client(models.Model):
    name = models.CharField("Name", max_length=31)
    email = models.EmailField("E-mail", max_length=255, unique=True)
    age = models.IntegerField("Age")
    country = models.ManyToManyField("Country")
    language = models.ManyToManyField("Language")
    payment = models.ManyToManyField("Payment")
    created_by = models.DateTimeField(auto_now_add=True)
    modified_by = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [ models.CheckConstraint(check=models.Q(age__gte=14), name='age_gte_14'), ]
        ordering = ['created_by', 'email']
        get_latest_by = 'created_by'

    def __str__(self):
        return self.secondname + self.age + self.country + self.email + self.programming_language + self.payment
    