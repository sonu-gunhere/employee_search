from typing import List, Optional
from fastapi import APIRouter, Query, Request, HTTPException
from app.schemas.enums import CompanyEnum, DepartmentEnum, LocationEnum, PositionEnum, StatusEnum
from app.services.search_services import SearchService
from app.utils.rate_limiter import is_allowed


router = APIRouter()


@router.get("/")
def search(
    request: Request,
    org_id: str = Query(...),
    query: str = Query(""),
    status: Optional[List[StatusEnum]] = Query(default=[]),
    location: List[LocationEnum] = Query(default=[]),
    company: List[CompanyEnum] = Query(default=[]),
    department: List[DepartmentEnum] = Query(default=[]),
    position: List[PositionEnum] = Query(default=[])
):
    user_ip = request.client.host
    user_key = f"{user_ip}"

    if not is_allowed(user_key):
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    return SearchService().search_employees(org_id, query, status, location, company, department, position)