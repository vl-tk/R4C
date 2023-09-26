import datetime
import http

from django.core import mail
from django.test import TestCase
from django.urls import reverse
from orders.models import Order, WaitingListItem
from robots.models import Robot


class RobotOrderTestCase(TestCase):
    def test_create_order(self):
        Robot.objects.create(
            model="R2",
            version="D2",
            created=str(datetime.datetime.now(datetime.timezone.utc)),
        )

        response = self.client.post(
            reverse("create_order"),
            data={"email": "test@example.com", "robot_serial": "R2 D2"},
        )

        self.assertEqual(response.status_code, http.HTTPStatus.CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(WaitingListItem.objects.count(), 0)

    def test_create_waiting_list_item(self):
        response = self.client.post(
            reverse("create_order"),
            data={"email": "test@example.com", "robot_serial": "R2 D2"},
        )

        self.assertEqual(response.status_code, http.HTTPStatus.CREATED)
        self.assertEqual(Order.objects.count(), 0)
        self.assertEqual(WaitingListItem.objects.count(), 1)

    def test_sending_waiting_list_item_email_sending(self):
        mail.outbox = []
        outbox = mail.outbox

        response = self.client.post(
            reverse("create_order"),
            data={"email": "test@example.com", "robot_serial": "R2 D2"},
        )

        self.assertEqual(response.status_code, http.HTTPStatus.CREATED)
        self.assertEqual(Order.objects.count(), 0)
        self.assertEqual(WaitingListItem.objects.count(), 1)

        Robot.objects.create(
            model="R2",
            version="D2",
            created=str(datetime.datetime.now(datetime.timezone.utc)),
        )

        self.assertEqual(len(outbox), 1)
        self.assertEqual(WaitingListItem.objects.count(), 0)
