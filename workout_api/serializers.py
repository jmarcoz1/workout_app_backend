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
    class Meta:
        model = Exercise
        fields = ["id", "name", "muscle"]


class SetSerializer(serializers.ModelSerializer):
    # exercise = serializers.StringRelatedField()
    class Meta:
        model = Set
        fields = ["id", "reps_in_reserve", "repetitions", "is_bodyweight", "weight_lifted", "exercise", "reps_in_reserve"]

class WorkoutSerializer(serializers.ModelSerializer):
    sets = SetSerializer(many=True)
    class Meta:
        model = Workout
        fields = ["id", "date", "user", "sets"]