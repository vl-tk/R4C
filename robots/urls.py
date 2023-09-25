from robots.views import create_robot, download_report_file
from django.urls import path

urlpatterns = [
    path("", create_robot, name="create_robot"),
    path(
        "excel_reports/summary_for_week.xlsx",
        download_report_file,
        name="download_report_file",
    ),
]
