from django.db import models


# Create your models here.
class Receitas(models.Model):
    img = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


    def __str__(self):
        return self.title
