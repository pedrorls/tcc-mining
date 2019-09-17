from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("new_teacher/", new_teacher, name="new_teacher"),
]

