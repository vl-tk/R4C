from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from robots.models import Robot
from robots.forms import RobotForm
import http


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
