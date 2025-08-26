import enum

class AppointmentStatus(enum.Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
    DONE = "DONE"

class ServiceCategory(enum.Enum):
    HAIR = "HAIR"
    NAILS = "NAILS"
    MAKEUP = "MAKEUP"
    OTHER = "OTHER"

class ServiceTechnique(enum.Enum):
    BASIC = "BASIC"
    ADVANCED = "ADVANCED"
    SPECIAL = "SPECIAL"

class RoleType(enum.Enum):
    OWNER = "OWNER"
    CLIENT = "CLIENT"
