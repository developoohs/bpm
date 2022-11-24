from typing import Optional,TypeVar
from pydantic import BaseModel

T = TypeVar('T')

class ProcessSchema(BaseModel):
    id:Optional[int]=None
    fk_unit_category:Optional[int]=None
    fk_unit:Optional[int]=None
    fk_unit_position:Optional[int]=None
    fk_demand_category:Optional[int]=None
    fk_demand_type:Optional[int]=None
    fk_demand:Optional[int]=None
    fk_demand_process:Optional[int]=None
    fk_demand_place:Optional[int]=None
    fk_check_category:Optional[int]=None
    fk_check_type:Optional[int]=None
    fk_check:Optional[int]=None
    fk_check_output:Optional[int]=None
    fk_process_estimation:Optional[int]=None
    fk_process_output:Optional[int]=None
    fk_script:Optional[int]=None
    fk_pointer_process:Optional[int]=None

    class Config:
        orm_mode = True


