from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r"^$", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]