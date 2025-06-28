from enum import Enum

class StatusEnum(str, Enum):
    active = "Active"
    not_started = "Not_started"
    terminated = "Terminated"


class LocationEnum(str, Enum):
    mumbai = "Mumbai"
    indore = "Indore"
    pune = "Pune"


class CompanyEnum(str, Enum):
    tcs = "TCS"
    infosys = "Infosys"
    hcl = "HCL"


class DepartmentEnum(str, Enum):
    hr = "HR"
    engineering = "Engineering"
    sales = "Sales"


class PositionEnum(str, Enum):
    manager = "Manager"
    developer = "Developer"
    executive = "Executive"
