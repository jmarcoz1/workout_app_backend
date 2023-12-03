from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User, Workout, Muscle, Exercise, Set
from .serializers import UserSerializer, WorkoutSerializer, MuscleSerializer, ExerciseSerializer, SetSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

class UserIDView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, name, format=None):
        user = get_object_or_404(User, name=name)
        return Response({'id': user.id})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    
    @action(detail=True, methods=['get'])
    def workouts(self, request, pk=None):
        user = self.get_object()
        workout = Workout.objects.filter(user=user)
        serializer = WorkoutSerializer(workout, many=True)
        return Response(serializer.data)

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    
    # def get_queryset(self):
    #     return Workout.objects.filter(user=self.request.user.name)

    @action(detail=True, methods=['get'])
    def sets(self, request, pk=None):
        workout = self.get_object()
        sets = Set.objects.filter(workout=workout)
        serializer = SetSerializer(sets, many=True)
        return Response(serializer.data)

class MuscleViewSet(viewsets.ModelViewSet):
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    
    @action(detail=True, methods=['get'])
    def exercises(self, request, pk=None):
        muscle = self.get_object()
        exercise = Exercise.objects.filter(muscle=muscle)
        serializer = ExerciseSerializer(exercise, many=True)
        return Response(serializer.data)

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    
    @action(detail=True, methods=['get'])
    def sets(self, request, pk=None):
        exercise = self.get_object()
        sets = Set.objects.filter(exercise=exercise)
        serializer = SetSerializer(sets, many=True)
        return Response(serializer.data)


class SetViewSet(viewsets.ModelViewSet):
    queryset = Set.objects.all()
    serializer_class = SetSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)
