from django.db import models


# Create your models here.

class Images(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    # images = models.ForeignKey(Images,on_delete=models.CASCADE, many=True)
    images = models.ManyToManyField(Images)

    def __str__(self):
        return self.name
