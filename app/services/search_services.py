


from typing import List, Optional
from app.models.dummy_data import EMPLOYEES, ORG_COLUMN_CONFIG
from app.schemas.enums import CompanyEnum, DepartmentEnum, LocationEnum, PositionEnum, StatusEnum


class SearchService:

    def __init__(self):
        pass

    def search_employees(
            self,
            org_id: str,
            query: str,
            status: Optional[List[StatusEnum]],
            location: Optional[List[LocationEnum]],
            company: Optional[List[CompanyEnum]],
            department: Optional[List[DepartmentEnum]],
            position: Optional[List[PositionEnum]]
        ):
        config = ORG_COLUMN_CONFIG.get(org_id)
        if not config:
            return []
        result = []
        for emp in EMPLOYEES:
            if query.lower() not in emp["name"].lower():
                continue
            if status and emp["status"] not in [s.value for s in status]:
                continue
            if location and emp["location"] not in [l.value for l in location]:
                continue
            if company and emp["company"] not in [c.value for c in company]:
                continue
            if department and emp["department"] not in [d.value for d in department]:
                continue
            if position and emp["position"] not in [p.value for p in position]:
                continue

            filtered = {k: v for k, v in emp.items() if k in config}
            result.append(filtered)

        return result