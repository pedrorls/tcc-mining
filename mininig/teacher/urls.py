from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("search/", search_result, name="search_result"),
    path("new_teacher/", new_teacher, name="new_teacher"),
]

