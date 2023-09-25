import logging
import openpyxl
from pathlib import Path

from django.conf import settings
from django.db.models import Count

from robots.models import Robot
from utils.date import get_last_monday

logger = logging.getLogger("django")


def delete_report(report_filepath="excel_reports/summary_for_week.xlsx"):
    # delete previous file
    report_file = Path(settings.BASE_DIR) / report_filepath
    report_file.unlink(missing_ok=True)


def create_report(report_filepath="excel_reports/summary_for_week.xlsx"):
    logger.info("create_report CALLED")

    # create summary file for recent robots created
    last_monday = get_last_monday()
    wb = openpyxl.Workbook()
    del wb["Sheet"]

    models_count = (
        Robot.objects.filter(created__gt=last_monday)
        .values("model")
        .annotate(total=Count("model"))
        .order_by("total")
    )
    for model_data in models_count:
        ws = wb.create_sheet(model_data["model"])

        ws["A1"] = "Версия"
        ws["B1"] = "Количество за неделю"

        versions_count = (
            Robot.objects.filter(created__gt=last_monday, model=model_data["model"])
            .values("version")
            .annotate(total=Count("version"))
            .order_by("total")
        )
        logger.info(versions_count)
        for n, version_data in enumerate(versions_count, start=1):
            ws[f"A{n + 1}"] = version_data["version"]
            ws[f"B{n + 1}"] = version_data["total"]

    wb.save(report_filepath)
    logger.info(f"{report_filepath} created. Status: OK")
