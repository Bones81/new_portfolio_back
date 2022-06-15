from django.urls import path
from . import views

urlpatterns = [
  path('api/projects', views.ProjectList.as_view(), name='project_list'),
  path('api/projects/<int:pk>', views.ProjectDetail.as_view(), name='project_detail'),
]