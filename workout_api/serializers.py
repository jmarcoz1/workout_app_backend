from rest_framework import serializers
from .models import Trainee, Workout, Muscle, Exercise, Set
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = ["name", "born_date"]

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ["date", "traineeId"]

class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = ["name"]

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["name", "involved_muscles"]

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ["intensity", "repetitions", "exerciseId", "workoutId"]