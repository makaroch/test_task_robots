from django.db.models.signals import pre_save
from django.dispatch import receiver

from robots.models import Robot
from robots.services.utils import get_robots_by_serial
from .utils import sends_emails


@receiver(pre_save, sender=Robot)
def notify_user_when_robot_available(sender, instance, **kwargs):
    serial_robot = instance.serial
    robots = get_robots_by_serial(serial_robot)

    if robots:
        return

    sends_emails(serial_robot)
