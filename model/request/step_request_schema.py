from typing import Optional
from pydantic import BaseModel



class UnitCategorySchema(BaseModel):
    id:Optional[int]=None
    unit_category : Optional[str]=None
    unit_category_description : Optional[str]=None
    unit_category_level: Optional[int]= None

    class Config:
        orm_mode = True

class UnitSchema(BaseModel):
    id:Optional[int]=None
    unit : Optional[str]=None
    unit_description : Optional[str]=None
    unit_level: Optional[int]= None

    class Config:
        orm_mode = True

class UnitPartSchema(BaseModel):
    id:Optional[int]=None
    unit_part : Optional[str]=None
    unit_part_description : Optional[str]=None

    class Config:
        orm_mode = True


class UnitPositionSchema(BaseModel):
    id:Optional[int] = None
    unit_position : Optional[str] = None
    unit_position_description : Optional[str] = None
    unit_position_level: Optional[int]= None

    class Config:
        orm_mode = True

class DemandCategorySchema(BaseModel):
    id:Optional[int] = None
    demand_category : Optional[str] = None
    demand_category_description : Optional[str] = None
    demand_category_level: Optional[int]= None

    class Config:
        orm_mode = True

class DemandTypeSchema(BaseModel):
    id:Optional[int] = None
    demand_type : Optional[str] = None
    demand_type_description : Optional[str] = None
    demand_type_level: Optional[int]= None

    class Config:
        orm_mode = True


class DemandSchema(BaseModel):
    id:Optional[int] = None
    demand : Optional[str] = None
    demand_description : Optional[str] = None
    demand_level: Optional[int]= None

    class Config:
        orm_mode = True

class DemandProcessSchema(BaseModel):
    id:Optional[int] = None
    demand_process : Optional[str] = None
    demand_process_description : Optional[str] = None
    demand_process_level: Optional[int]= None

    class Config:
        orm_mode = True

class DemandPlaceSchema(BaseModel):
    id:Optional[int] = None
    demand_place : Optional[str] = None
    demand_place_description : Optional[str] = None
    demand_place_level: Optional[int]= None

    class Config:
        orm_mode = True


class CheckCategorySchema(BaseModel):
    id:Optional[int] = None
    check_category : Optional[str] = None
    check_category_description : Optional[str] = None
    check_category_level: Optional[int]= None

    class Config:
        orm_mode = True

class CheckTypeSchema(BaseModel):
    id:Optional[int] = None
    check_type : Optional[str] = None
    check_type_description : Optional[str] = None
    check_type_level: Optional[int]= None

    class Config:
        orm_mode = True

class CheckSchema(BaseModel):
    id:Optional[int] = None
    check : Optional[str] = None
    check_description : Optional[str] = None
    check_level: Optional[int]= None

    class Config:
        orm_mode = True

class CheckOutputSchema(BaseModel):
    id:Optional[int] = None
    check_output : Optional[str] = None
    check_output_description : Optional[str] = None
    check_output_level: Optional[int]= None

    class Config:
        orm_mode = True

class ProcessEstimationSchema(BaseModel):
    id:Optional[int] = None
    process_estimation : Optional[str] = None
    process_estimation_description : Optional[str] = None
    process_estimation_level: Optional[int]= None

    class Config:
        orm_mode = True

class ProcessOutputSchema(BaseModel):
    id:Optional[int] = None
    process_output : Optional[str] = None
    process_output_desription : Optional[str] = None
    process_output_level: Optional[int]= None

    class Config:
        orm_mode = True

class ScriptSchema(BaseModel):
    id:Optional[int] = None
    script : Optional[str] = None
    script_description : Optional[str] = None
    script_level: Optional[int]= None

    class Config:
        orm_mode = True

def request_dict(tableName:str):
    request_step_dict= {
        "unit_category":UnitCategorySchema ,"unit":UnitSchema,"unit_part":UnitPartSchema,"unit_position":UnitPositionSchema,
        "demand_category":DemandCategorySchema,"demand_type":DemandTypeSchema,"demand":DemandSchema,"demand_process":DemandProcessSchema,"demand_place":DemandPlaceSchema,
        "check_category":CheckCategorySchema,"check_type":CheckTypeSchema,"check":CheckSchema,"check_output":CheckOutputSchema,
        "process_estimation":ProcessEstimationSchema,"process_output":ProcessOutputSchema,"script":ScriptSchema}
    return request_step_dict[tableName]