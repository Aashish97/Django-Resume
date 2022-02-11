from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r"^$", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]