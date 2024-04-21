from django.db import models


class DayOldChicksOrder(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    location = models.CharField(max_length=300)
    layers = models.BooleanField()
    broilers = models.BooleanField()
    kenbros = models.BooleanField()
    numberOfBirds = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
