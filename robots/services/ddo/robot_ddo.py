from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class RobotDDO:
    model: str
    version: str
    created: str
    serial: str | None = field(init=False, default=None)
    id: int | None = field(init=False, default=None)

    def __post_init__(self):
        if self.serial is None:
            self.serial = f"{self.model}-{self.version}"
        self.validate_date()
        self.validate_types()
        self.validate_length()

    def validate_date(self):
        try:
            datetime.strptime(self.created, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD HH:MM:SS")

    def validate_types(self):
        if not isinstance(self.model, str):
            raise ValueError("Model must be a string")
        if not isinstance(self.version, str):
            raise ValueError("Version must be a string")
        if not isinstance(self.created, str):
            raise ValueError("Created must be a string")

    def validate_length(self):
        if len(self.model) != 2:
            raise ValueError("Model must be 2 characters long")
        if len(self.version) != 2:
            raise ValueError("Version must be 2 characters long")
