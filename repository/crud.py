from sqlalchemy.orm import Session

#REQUEST/CAST_MODEL
from model.request.process_request_schema import *
from model.request.step_request_schema import *
#DB_MODEL
from model.db.process_db_model import *
from model.db.step_db_model import *
#interface_request_model
from model.interface.request_interface import Idb


from sqlalchemy.exc import DontWrapMixin

from sqlalchemy.exc import SQLAlchemyError



def db_create(db:Session,table:Idb):
    try:
        db.add(table)
        db.commit()
        db.refresh(table)
        db.close()
    except SQLAlchemyError as error:
        db.rollback()
        db.close()
        return str(error.__dict__["orig"])
    return table

def db_get_item(db:Session,table:str):
    return db.query(table).offset(0).all()

def db_item_by_id(db:Session,table_name,id_column_name,id):
    return db.query(table_name).filter(id_column_name == id).first()

def db_del_item(db:Session,db_model,column_name,id):
    try:
        db.query(db_model).filter(column_name == id).delete()
        db.commit()
    except Exception as error:
        print(error)

    #return db.query(table_name).filter(table_name.id == id).delete()

def db_update_item(db:Session,table_name,column_name,id,value):
    db.query(table_name).filter(column_name == id).update(value)
    db.commit()
    return db.query(table_name).filter(column_name == id).first()


def db_inner_query(db:Session,table_name,fk_column_name,id_column_name,id):
    result= db.query(table_name).join(Process).filter(fk_column_name == id_column_name).filter( id_column_name == id).all()
    return result







