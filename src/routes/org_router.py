from fastapi import APIRouter, Depends, HTTPException
from src.database.session import get_db
from sqlalchemy.orm import Session
from src.models.org.schemas import (
    OrgCreateDTO,
    OrgSerializer,
    OrgAccessor,
    OrgResponse,
    OrgUpdateDTO,
)

router = APIRouter()


@router.post("/create_org", response_model=OrgResponse)
def create_org(
    *,
    db: Session = Depends(get_db),
    dummy_org_in: OrgCreateDTO,
):
    dummy_org_ = OrgSerializer.create(org_name=dummy_org_in.org_name)
    OrgAccessor.add(entity=dummy_org_, db_session=db)
    return dummy_org_


@router.put("/{org_id}", response_model=OrgResponse)
def create_org_user_relation(
    *,
    db: Session = Depends(get_db),
    org_id: int,
    update_org_dto: OrgUpdateDTO,
):
    org = OrgAccessor.get_by_id(resource_id=org_id, db_session=db)
    cs = org.update(update_org=update_org_dto)
    OrgAccessor.update_by_id(resource_id=org_id, change_set=cs, db_session=db)
    return org


@router.get("/get_org_details", response_model=OrgResponse)
def get_org_details(
    *,
    db: Session = Depends(get_db),
    org_id: int,
):
    try:
        org_ = OrgAccessor.get_by_id(resource_id=org_id, db_session=db)
    except Exception as err:
        raise HTTPException(status_code=404, detail="Org not found")
    return org_
