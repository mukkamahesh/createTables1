from django.db import models

# Create your models here.
class mahesh(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
class loki(models.Model):
    name=models.ForeignKey(mahesh,on_delete=models.CASCADE)
    rollnum=models.IntegerField()
class suresh(models.Model):
    rollnum=models.ForeignKey(loki,on_delete=models.CASCADE)
    age=models.CharField(max_length=100)
    email=models.EmailField()

