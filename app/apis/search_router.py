from typing import List, Optional
from fastapi import APIRouter, Query, Request, HTTPException

from app.utils.rate_limiter import rate_limit
from app.services.search_services import SearchService
from app.schemas.enums import CompanyEnum, DepartmentEnum, LocationEnum, PositionEnum, StatusEnum


router = APIRouter()


@router.get("/")
@rate_limit
async def search(
    request: Request,
    org_id: str = Query(...),
    query: str = Query(""),
    status: Optional[List[StatusEnum]] = Query(default=[]),
    location: List[LocationEnum] = Query(default=[]),
    company: List[CompanyEnum] = Query(default=[]),
    department: List[DepartmentEnum] = Query(default=[]),
    position: List[PositionEnum] = Query(default=[])
):
    search_service = SearchService()
    return await search_service.search_employees(org_id, query, status, location, company, department, position)