from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_shown, name="project_shown"),
    path("<int:pk>/", views.project_info, name="project_info"),
]