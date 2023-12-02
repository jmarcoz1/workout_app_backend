"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import  UserViewSet, WorkoutViewSet, MuscleViewSet, ExerciseViewSet, SetViewSet

router = routers.DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'workout', WorkoutViewSet)
router.register(r'muscles', MuscleViewSet)
router.register(r'exercise', ExerciseViewSet)
router.register(r'set', SetViewSet)

urlpatterns = [
    path('', include(router.urls))
]
