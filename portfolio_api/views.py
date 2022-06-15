from django.shortcuts import render
from portfolio_api.serializers import ProjectSerializer
from rest_framework import generics
from .models import Project
# Create your views here.

class ProjectList(generics.ListCreateAPIView):
  queryset = Project.objects.all().order_by('id')
  serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Project.objects.all().order_by('id')
  serializer_class = ProjectSerializer
