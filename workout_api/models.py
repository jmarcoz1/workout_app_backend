from django.db import models
from datetime import date

# Create your models here.

class Trainee(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField(editable=True)
    def __str__(self):
        return self.name

class Workout(models.Model):
    date = models.DateField(auto_now_add=True)
    traineeId = models.ForeignKey(Trainee, on_delete = models.CASCADE, blank = True, null = True)

class Muscle(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField("name of the exercise", max_length=200)
    involved_muscles = models.ManyToManyField(Muscle)
    def __str__(self):
        return self.name

class Set(models.Model):
    intensity = models.SmallIntegerField()
    comments = models.CharField(max_length=200)
    repetitions = models.SmallIntegerField()
    is_bodyweight = models.BooleanField()
    weight = models.DecimalField(max_digits=4,decimal_places=2)
    exerciseId = models.ManyToManyField(Exercise)
    workoutId = models.ForeignKey(Workout, on_delete = models.CASCADE, blank = True, null = True)
