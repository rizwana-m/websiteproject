from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()


    def __str__(self):
        return self.name

class Teams(models.Model):
    image=models.ImageField(upload_to='pics')
    title=models.CharField(max_length=200)
    about=models.TextField(max_length=500)


    def __str__(self):
        return self.title