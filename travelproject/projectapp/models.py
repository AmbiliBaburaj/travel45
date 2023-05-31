from django.db import models

class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
    def __str__(self):
        return self.name
class Team(models.Model):

    img1=models.ImageField(upload_to='pics')
    name1 = models.CharField(max_length=250)
    desc1=models.TextField()
    def __str__(self):
        return self.name1