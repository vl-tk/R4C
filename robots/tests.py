from django.test import TestCase
import requests
import http
from robots.models import Robot
from django.urls import reverse


class RobotTestCase(TestCase):
    def test_create_robots(self):
        data = (
            {"model": "R2", "version": "D2", "created": "2022-12-31 23:59:59"},
            {"model": "13", "version": "XS", "created": "2023-01-01 00:00:00"},
            {"model": "X5", "version": "LT", "created": "2023-01-01 00:00:01"},
        )

        for item_data in data:
            response = self.client.post(reverse("create_robot"), data=item_data)
            self.assertEqual(response.status_code, http.HTTPStatus.CREATED)

        self.assertEqual(Robot.objects.count(), 3)
