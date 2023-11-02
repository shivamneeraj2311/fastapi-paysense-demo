import datetime
from varname import nameof

from src.models import accessor as accessor
from src.database import orm
from typing import Optional
from pydantic import BaseModel
from src.models import entity
from src.models.id_prefix import IdPrefix
from src.models.id import  IdStr
from src.common_utils.date_utils import get_utc_now
from src.models.users.user import UserID

class OrgID(IdStr):
    prefix = IdPrefix.DUMMY_ORG

class OrgBaseDTO(BaseModel):
    org_name: Optional[str] = None


# Properties to receive on item creation
class OrgCreateDTO(OrgBaseDTO):
    ...


# Properties to receive on item update
class OrgUpdateDTO(OrgBaseDTO):
    user_id: Optional[UserID] = None


# Properties shared by models stored in DB
class OrgSerializer(entity.Entity):
    id: OrgID
    org_name: str
    created_date: datetime.datetime
    updated_date: datetime.datetime
    dummy_user_id: Optional[UserID]

    @classmethod
    def create(cls, *, org_name: str):
        dummy_org_id = OrgID.make()
        created_date = get_utc_now()
        updated_date = get_utc_now()
        org_name = org_name


        return cls(
            id=dummy_org_id, org_name=org_name, created_date=created_date,
            updated_date=updated_date
        )

    def update(self, *, update_org: OrgUpdateDTO) -> accessor.ChangeSet:
        self.dummy_user_id = update_org.user_id
        self.updated_date = get_utc_now()
        return {
            nameof(self.dummy_user_id): self.dummy_user_id
        }


# API Response Model
class OrgResponse(OrgSerializer):
    pass

class OrgAccessor(
    accessor.Accessor[orm.Org, OrgSerializer, OrgID]
):
    orm_table = orm.Org
    entity = OrgSerializer



