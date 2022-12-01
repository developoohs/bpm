from pydantic import BaseModel,Field
#DB_MODELS
from model.db.process_db_model import Process
from model.db.step_db_model import *

from repository.crud import db_inner_query




#bir tablo adı alıyor ve clientten gelen sözlük tipindeki değeri  alıyor
#db_model_dict fonksiyonu karşılık gelen
def db_model_cast(table_name:str ,value:dict=None):
#veritabanına kayıt edilmesi için clientten gelen sözlükteki value değerlerinin kayıt edilecek veritabanı modeline set edilmesi gerekiyor
#burada db_model_dict sözlüğünden çağırılan ve clientten gönderilen tablo adının karşılığı sınıf db_model'e değer olarak atanıyor
    db_model = db_model_dict(table_name)
    #ve db_model'in değeri olan sınıf çağırılarak, clientten gelen sözlük tipinde değerler sınıfa set ediliyor.
    value = db_model(**value)
    return value

def db_id_value(request:dict):
    table_name =request.table_name
    value = request.value
    column_name= list(value.keys())[0]
    column_value = value[column_name]
    db_model=db_model_dict(table_name)
    column_name = eval(db_model.__name__ +"."+column_name)
    return db_model,column_name,column_value

def update_request_solve_for_save(request:dict):
    table_name =request.table_name
    value = request.value
    column_name= list(value.keys())[0]
    id_column_value = value[column_name]
    del value[column_name]
    db_model=db_model_dict(table_name)
    column_name = eval(db_model.__name__ +"."+column_name)
    return db_model,column_name,id_column_value,value


def edit_inner_result(result:dict):
    #client'e gönderilecek veriye ait sözlüğün gereksiz olan ögesini siliyor.
    result =vars(result[0])
    counter = 0
    for i in result:
        counter +=1
        if counter ==1:
            del result[i]
            break
    return result



def inner_create(db,value):
    response_dict={}
    for v in value:
        table_name=v["table_name"]
        #sqlalchemy model dict
        db_model = db_model_dict(table_name)
        #python nesnesi olarak çağırılan sütun ismi
        column_name = eval(db_model.__name__ +"."+v["column_name"])
        #python nesnesi olarak çağırılan fk_sütun ismi
        fk_column_name = eval("Process" +".fk_"+ table_name)
        #client'ten gelen sütun değeri
        column_value = v["column_value"]
        #inner join işlemi
        result = db_inner_query(db,db_model,fk_column_name,column_name,column_value)
        if result != []:
            response_value = edit_inner_result(result)
            response_dict["table_name"] = table_name
            response_dict["value"] = response_value
        else:
            response_dict ="bulunamadı"
            return response_dict
    return response_dict




"""def db_model_cast_for_db(table_name:str ,value:dict):
    #request_dict()
    db_model= db_model_dict(table_name)
    return db_model(**value)"""