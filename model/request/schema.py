from typing import List,Optional,Generic,TypeVar
from pydantic import BaseModel,Field
from pydantic.generics import GenericModel

#from .process_schemas import *


T = TypeVar('T')

class Request(BaseModel):
    parameter: Optional[T] = Field(...)


class Response(GenericModel,Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]