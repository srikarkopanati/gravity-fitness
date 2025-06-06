from django.db import models
from django.contrib.auth.models import User

class FitnessClass(models.Model):
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    available_slots = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} on {self.datetime}"

class Booking(models.Model):
    fitness_class = models.ForeignKey(FitnessClass, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)  # Allowing +91 and 10-digit number

    def __str__(self):
        return f"{self.user.username} - {self.fitness_class.name}"
