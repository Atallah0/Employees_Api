from django.db import models

class Employees(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name