from django.db import models
from datetime import date

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField(editable=True)
    def __str__(self):
        return self.name

class Muscle(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Exercise(models.Model):
    name = models.CharField("name of the exercise", max_length=200)
    muscle = models.ForeignKey(Muscle, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Set(models.Model):
    reps_in_reserve = models.IntegerField()
    comments = models.CharField(max_length=200)
    repetitions = models.IntegerField()
    is_bodyweight = models.BooleanField()
    weight_lifted = models.FloatField(max_digits=4,decimal_places=2)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.repetitions} reps of {self.exercise.name}'

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    sets = models.ManyToManyField(Set)

    def __str__(self):
        return f'Workout on {self.date} by {self.user.username}'