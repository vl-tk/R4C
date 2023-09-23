from robots.views import create_robot
from django.urls import path

urlpatterns = [
    path("", create_robot, name="create_robot"),
]
