from django.db import models

# Create your models here.
class hydjobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length = 100)
    job_title = models.CharField(max_length = 100)
    eligibility = models.CharField(max_length = 30)
    address = models.CharField(max_length = 100)
    email = models.EmailField()
    phone_number = models.IntegerField()

class punejobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length = 100)
    job_title = models.CharField(max_length = 100)
    eligibility = models.CharField(max_length = 30)
    address = models.CharField(max_length = 100)
    email = models.EmailField()
    phone_number = models.IntegerField()

class delhijobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length = 100)
    job_title = models.CharField(max_length = 100)
    eligibility = models.CharField(max_length = 30)
    address = models.CharField(max_length = 100)
    email = models.EmailField()
    phone_number = models.IntegerField()
