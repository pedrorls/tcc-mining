from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("upload/", upload_curriculum, name="upload_curriculum"),
]

