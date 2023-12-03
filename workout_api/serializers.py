from rest_framework import serializers
from .models import User, Workout, Muscle, Exercise, Set

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "birth_date"]


class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = ["id", "name"]


class ExerciseSerializer(serializers.ModelSerializer):
    muscle = MuscleSerializer(read_only=True)
    class Meta:
        model = Exercise
        fields = ["id", "name", "muscle"]

class WorkoutSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Workout
        fields = ["id", "date", "user"]

class SetSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(read_only=True)
    workout = WorkoutSerializer(read_only=True)
    class Meta:
        model = Set
        fields = ["id", "reps_in_reserve", "repetitions", "is_bodyweight", "weight_lifted", "exercise", "reps_in_reserve", "workout"]