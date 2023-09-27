import http
import mimetypes
from pathlib import Path

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from robots.forms import RobotForm
from robots.models import Robot
from robots.services import create_report, delete_report


@csrf_exempt
def create_robot(request):
    if request.POST:
        form = RobotForm(request.POST)
        if form.is_valid():
            robot = Robot.objects.create(
                model=request.POST.get("model"),
                version=request.POST.get("version"),
                created=request.POST.get("created"),
            )
        else:
            return JsonResponse(
                {"message": form.errors}, status=http.HTTPStatus.BAD_REQUEST
            )

        return JsonResponse(
            {"message": f"{robot} created succesfully"},
            status=http.HTTPStatus.CREATED,
        )

    return JsonResponse(
        {"message": "Use POST request to create a robot"},
        status=http.HTTPStatus.BAD_REQUEST,
    )


def download_report_file(request):
    try:
        delete_report()
        create_report()  # for simple reports only
    except Exception as e:
        return JsonResponse(
            {"message": "Error creating report"},
            status=http.HTTPStatus.INTERNAL_SERVER_ERROR,
        )
    full_path = Path("excel_reports/summary_for_week.xlsx")
    with open(full_path, "rb") as f:
        mime_type, _ = mimetypes.guess_type(full_path)
        response = HttpResponse(f, content_type=mime_type)
        response["Content-Disposition"] = "attachment; filename=%s" % full_path.name
    return response
