from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    coursecode =  models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name