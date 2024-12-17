from django.http import QueryDict

from robots.models import Robot
from robots.services import RobotDDO


def validate_data_robot(data: QueryDict) -> RobotDDO:
    model = data.get("model", None)
    version = data.get("version", None)
    created = data.get("created", None)
    return RobotDDO(
        model=model,
        version=version,
        created=created,
    )


def save_new_robot(robot: RobotDDO) -> None:
    Robot.objects.create(
        serial=robot.serial,
        model=robot.model,
        version=robot.version,
        created=robot.created
    )
