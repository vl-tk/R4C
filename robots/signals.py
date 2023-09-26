import logging

from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import WaitingListItem
from robots.models import Robot
from utils.email import send_waiting_list_email

logger = logging.getLogger("django")


@receiver(post_save, sender=Robot, dispatch_uid="inform_about_robot_availability")
def robot_created(sender, instance, created, **kwargs):
    if created:
        items = WaitingListItem.objects.filter(robot_serial=instance.serial)
        for item in items:
            try:
                send_waiting_list_email(
                    [item.customer.email], instance.model, instance.version
                )
            except Exception:
                pass
            else:
                item.delete()
