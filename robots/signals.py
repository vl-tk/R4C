import logging

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from robots.models import Robot

logger = logging.getLogger("django")
