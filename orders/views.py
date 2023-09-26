import http

from customers.models import Customer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order, WaitingListItem
from robots.models import Robot


def _create_customer(email):
    return Customer.objects.create(email=email)


@csrf_exempt
def create_order(request):
    customer = _create_customer(request.POST["email"])

    try:
        robot = Robot.objects.get(serial=request.POST["robot_serial"])
    except Robot.DoesNotExist:
        WaitingListItem.objects.create(
            customer=customer, robot_serial=request.POST["robot_serial"]
        )

        return JsonResponse(
            {"message": "We've added you to the waiting list for this robot"},
            status=http.HTTPStatus.CREATED,
        )
    else:
        order = Order.objects.create(robot_serial=robot.serial, customer=customer)

    return JsonResponse(
        {"message": f"Order {order.pk} for {order.robot_serial} created succesfully"},
        status=http.HTTPStatus.CREATED,
    )
