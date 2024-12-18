from django.core.mail import send_mail

from R4C.settings import EMAIL_HOST_USER
from .models import Order
from .constants import SUBJECT_EMAIL, TEXT_EMAIL


def get_all_user_email_in_orders_by_serial(serial: str) -> list[str]:
    return (
        Order.objects
        .filter(robot_serial=serial)
        .select_related('customer')
        .values_list('customer__email', flat=True)
    )


def sends_emails(serial_robot: str) -> None:
    emails = get_all_user_email_in_orders_by_serial(serial_robot)
    if emails:
        subject = SUBJECT_EMAIL.format(serial_robot)
        message = TEXT_EMAIL.format(*serial_robot.split("-"))
        send_mail(
            subject,
            message,
            EMAIL_HOST_USER,
            emails
        )
