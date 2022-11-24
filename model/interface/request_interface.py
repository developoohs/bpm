from typing import List,Optional,Generic,TypeVar
from pydantic import BaseModel,Field
from pydantic.generics import GenericModel


T = TypeVar('T')

class Irequest(BaseModel,Generic[T]):
    parameter: Optional[T] = Field(...)

class Idb(BaseModel,Generic[T]):
    parameter: Optional[T] = Field(...)


class Iresponse(GenericModel,Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]


class RequestItem(BaseModel):
    table_name : str = None
    #value değerini request_model_cast'e gönder
    value:dict = None

class RequestItemForInner(BaseModel):
    table_name : str = None
    #value değerini request_model_cast'e gönder
    value:List = None

class RequestForId(BaseModel):
    table_name : str = None
    #value değerini request_model_cast'e gönder
    value:int = None