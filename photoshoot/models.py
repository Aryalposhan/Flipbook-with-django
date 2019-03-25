from django.db import models
from django.utils import timezone 


class  Gallery2018_19(models.Model):
    image = models.ImageField(blank=True, upload_to='static/uploads/2018_19')
    caption= models.CharField(max_length=1000)
    image_date= models.DateField()
    date = models.DateTimeField("date logged")


class Gallery2017_18(models.Model):
    image = models.ImageField(blank=True, upload_to='static/uploads/2017_18')
    caption= models.CharField(max_length=1000)
    image_date= models.DateField()
    date = models.DateTimeField("date logged")

class Gallery2016_17(models.Model):
    image = models.ImageField(blank=True, upload_to='static/uploads/2016_17')
    caption= models.CharField(max_length=1000)
    image_date= models.DateField()
    date = models.DateTimeField("date logged")

class Gallery2015_16(models.Model):
    image = models.ImageField(blank=True, upload_to='static/uploads/2015_16')
    caption= models.CharField(max_length=1000)
    image_date= models.DateField()
    date = models.DateTimeField("date logged")



    def __str__ (self):
        date_local = timezone.localtime(self.date)
        return f"'{self.image}' logged on{ date_local.strftime('%A,%d %B,%Y at %X')}"

# Create your models here.
