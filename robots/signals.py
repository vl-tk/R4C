import logging

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from services import create_report, delete_report

from robots.models import Robot

logger = logging.getLogger("django")


@receiver(post_delete, sender=Robot)
def on_delete(sender, instance, **kwargs):
    delete_report()
    create_report()


@receiver(post_save, sender=Robot)
def on_save(sender, instance, created, **kwargs):
    if created:
        delete_report()
        create_report()
