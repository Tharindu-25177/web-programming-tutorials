from django.db import models

class Position(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_specialist = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(blank=True)
    specialist_eligible = models.BooleanField(default=False)
    positions = models.ManyToManyField(Position, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
