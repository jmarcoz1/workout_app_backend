from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Trainee, Workout, Muscle, Exercise, Set
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer, TraineeSerializer, WorkoutSerializer, MuscleSerializer, ExerciseSerializer, SetSerializer
from rest_framework import viewsets

# Create your views here.

class MuscleListApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        muscle = Muscle.objects.filter(name = request.muscle.name)
        serializer = MuscleSerializer(muscle, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'name': request.data.get('name')
        }
        serializer = MuscleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer