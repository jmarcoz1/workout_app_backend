from rest_framework import serializers
from .models import Trainee, Workout, Muscle, Exercise, Set

class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = ["id", "name", "birth_date"]


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ["id", "date", "traineeId"]


class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = ["id", "name"]


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["id", "name", "involved_muscles"]


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = ["id", "intensity", "repetitions", "is_bodyweight", "weight", "exerciseId", "workoutId"]
