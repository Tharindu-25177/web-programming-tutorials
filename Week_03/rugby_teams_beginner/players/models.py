from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=100)
    specialist = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    positions = models.ManyToManyField(Position, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
