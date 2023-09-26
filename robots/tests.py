from django.test import TestCase
from pathlib import Path
import http
import datetime
from robots.models import Robot
from django.urls import reverse
from robots.services import create_report, delete_report


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


class RobotReportTestCase(TestCase):
    def test_creating_empty_report_no_robots_data(self):
        create_report("excel_reports/test_summary_for_week.xlsx")

        self.assertFalse(Path("excel_reports/test_summary_for_week.xlsx").exists())

    def test_create_report(self):
        r = Robot.objects.create(
            model="R2", version="D2", created=str(datetime.datetime.now())
        )
        r = Robot.objects.create(
            model="R2", version="D2", created=str(datetime.datetime.now())
        )
        r = Robot.objects.create(
            model="R2", version="D3", created=str(datetime.datetime.now())
        )
        r = Robot.objects.create(
            model="R2", version="D4", created=str(datetime.datetime.now())
        )

        create_report("excel_reports/test_summary_for_week.xlsx")

        self.assertTrue(Path("excel_reports/test_summary_for_week.xlsx").exists())

        delete_report("excel_reports/test_summary_for_week.xlsx")
