from fastapi import APIRouter,HTTPException,Path,Depends
from config import SessionLocal
from sqlalchemy.orm import Session

from service.request_cast import inner_create,db_model_cast,db_id_value,update_request_solve_for_save
from model.interface.request_interface import Iresponse,RequestItem,RequestItemForInner
from repository.crud import db_create,db_get_item,db_item_by_id,db_del_item,db_update_item
from model.db.step_db_model import db_model_dict

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

# ALL TABLE ITEMS CAN BE CREATED FROM THIS ROUTE
@router.post('/create')
async def create(request:RequestItem,db:Session=Depends(get_db)):
    cast_value= db_model_cast(request.table_name,request.value)
    response = db_create(db,cast_value)
    return Iresponse(code=200,status="",message="",result=response)

# VIEW all data IN THE TABLE
@router.post('/get_all_item')
async def get_all_item(request:RequestItem,db:Session=Depends(get_db)):
    cast_value= db_model_dict(request.table_name)
    item=db_get_item(db,cast_value)
    return Iresponse(code=200,status="Ok",message="Success Fetch Data",result=item).dict(exclude_none=True)

# :: QUERY AND DİSPLAY AND TABLE by id
@router.post('/get_item_by_id/{id}')
async def get_item_by_id(request:RequestItem,db:Session=Depends(get_db)):
    db_model,column_name,column_value = db_id_value(request)
    #create_id_column =db_id_column(table_name)
    item= db_item_by_id(db,db_model,column_name,column_value)
    return Iresponse(code=200,status="Ok",message="Success Fetch Data",result=item).dict(exclude_none=True)

# :: ALL TABLES CAN BE deleted FROM THIS ROUTER.
@router.post('/delete_item_by_id/{id}')
async def delete_item_by_id(request:RequestItem,db:Session=Depends(get_db)):
    db_model,column_name,column_value = db_id_value(request)
    db_del_item(db,db_model,column_name,column_value)
    return Iresponse(code=200,status="Ok",message="Deleted Data").dict(exclude_none=True)

# :: ALL TABLES CAN BE updated FROM THIS ROUTER.
@router.post('/update_item_by_id/{id}')
async def update_item_by_id(request:RequestItem,db:Session=Depends(get_db)):
    db_model,column_name,column_value,update_value = update_request_solve_for_save(request)
    response_item= db_update_item(db,db_model,column_name,column_value,request.value)
    return Iresponse(code=200,status="Ok",message="Updated Data",result=response_item).dict(exclude_none=True)

# :: INNER PROCESS for VIEWING THE PROCESS
@router.post('/get_inner_table')
async def get_inner_table(request:RequestItemForInner,db:Session=Depends(get_db)):
    value = request.value
    response_value = inner_create(db,value)
    return Iresponse(code=200,status="Ok",message="inner table Data",result=response_value).dict(exclude_none=True)



