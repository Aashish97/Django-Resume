from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.education_index.as_view(), name="education_index"),
]