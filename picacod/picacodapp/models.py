from django.db import models

# Create your models here.


class Jobs(models.Model):
    title=models.CharField(max_length=200)
    skills=models.TextField()
    no_of_vaccancies=models.IntegerField()
    min_experience=models.IntegerField(null=True)
    max_experience=models.IntegerField(null=True)

class Applications(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    designation=models.CharField(max_length=200)
    message=models.TextField()
    resume=models.FileField(upload_to='resumes/')