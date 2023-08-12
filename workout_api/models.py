from django.db import models

# Create your models here.

class Muscle(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    pass

class Exercise(models.Model):
    name = models.CharField("name of the exercise", max_length=200)
    muscles = models.ManyToManyField(Muscle, verbose_name="muscle that is involved in the exercise")
    pass

class PerformedExercise(models.Model):
    
    pass

class Workout(models.Model):
    pass

class Trainee(models.Model):
    pass




