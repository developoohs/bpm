from sqlalchemy import Column,Integer,String,ForeignKey,Text,SmallInteger
from config import Base
from model.db.process_db_model import Process

class UnitCategory(Base):
    __tablename__ = "unit_category"

    unit_category_id = Column(Integer,primary_key=True)
    unit_category = Column(String,unique=True)
    description = Column(Text,unique=True)
    level = Column(SmallInteger)

class Unit(Base):
    __tablename__ = "unit"

    unit_id = Column(Integer,primary_key=True)
    unit = Column(String,unique=True)
    description = Column(Text,unique=True)
    level = Column(SmallInteger)



class UnitPart(Base):
    __tablename__ = "unit_part"

    unit_part_id = Column(Integer,primary_key=True)
    unit_part= Column(String,unique=True)
    description = Column(Text,unique=True)


class UnitPosition(Base):
    __tablename__ = "unit_position"

    unit_position_id = Column(Integer,primary_key=True)
    unit_position = Column(String,unique=True)
    description = Column(Text,unique=True)
    level = Column(SmallInteger)



class DemandCategory(Base):
    __tablename__ = "demand_category"

    demand_category_id = Column(Integer,primary_key=True)
    demand_category = Column(String,unique=True)
    description = Column(Text,unique=True)
    level = Column(SmallInteger)

class DemandType(Base):
    __tablename__ = "demand_type"

    demand_type_id = Column(Integer,primary_key=True)
    demand_type = Column(String,unique=True)
    description = Column(Text,unique=True)
    level = Column(SmallInteger)


class Demand(Base):
    __tablename__ = "demand"

    demand_id = Column(Integer,primary_key=True)
    demand = Column(String,unique=True)
    description = Column(Text,unique=True)
    level = Column(SmallInteger)


class DemandProcess(Base):
    __tablename__ = "demand_process"

    demand_process_id = Column(Integer,primary_key=True)
    demand_process = Column(String,unique=True)
    description = Column(Text,unique=True)
    level = Column(SmallInteger)

class DemandPlace(Base):

    __tablename__ = "demand_place"

    demand_place_id = Column(Integer,primary_key=True)
    demand_place = Column(String,unique=True)
    description = Column(Text,unique=True)
    level = Column(SmallInteger)


class CheckCategory(Base):

    __tablename__ = "check_category"

    check_category_id = Column(Integer,primary_key=True)
    check_category = Column(String,unique=True)
    description = Column(Text,unique=True)
    level = Column(SmallInteger)

class CheckType(Base):

    __tablename__ = "check_type"

    check_type_id = Column(Integer,primary_key=True)
    check_type = Column(String,unique=True)
    description = Column(Text,unique=True)
    level = Column(SmallInteger)


class CheckItem(Base):

    __tablename__ = "check_item"

    check_item_id = Column(Integer,primary_key=True)
    check_item = Column(String,unique=True)
    description = Column(Text,unique=True)
    level = Column(SmallInteger)


class CheckOutput(Base):
    __tablename__ = "check_output"

    check_output_id = Column(Integer,primary_key=True)
    check_output = Column(String,unique=True)
    description = Column(Text,unique=True)
    level = Column(SmallInteger)


class ProcessEstimation(Base):
    __tablename__ = "process_estimation"

    process_estimation_id = Column(Integer,primary_key=True)
    process_estimation = Column(String,unique=True)
    description = Column(Text,unique=True)
    level = Column(SmallInteger)


class ProcessOutput(Base):
    __tablename__ = "process_output"

    process_output_id = Column(Integer,primary_key=True)
    process_output = Column(String,unique=True)
    description = Column(Text,unique=True)
    level = Column(SmallInteger)

class Script(Base):
    __tablename__ = "script"

    script_id = Column(Integer,primary_key=True)
    script = Column(String,unique=True)
    description = Column(Text,unique=True)
    level = Column(SmallInteger)

def db_model_dict(table_name:str):
    #"process":Process,
    response_step_dict={"process":Process,
        "unit_category":UnitCategory,"unit":Unit,"unit_part":UnitPart,"unit_position":UnitPosition,
        "demand_category":DemandCategory,"demand_type":DemandType,"demand":Demand,"demand_process":DemandProcess,
        "demand_place":DemandPlace,"check_category":CheckCategory,"check_type":CheckType,"check_item":CheckItem,
        "check_output":CheckOutput,"process_estimation":ProcessEstimation,"process_output":ProcessOutput,"script":Script}
    return response_step_dict[table_name]

response_step_dict={
    "unit_category":UnitCategory,"unit":Unit,"unit_part":UnitPart,"unit_position":UnitPosition,
    "demand_category":DemandCategory,"demand_type":DemandType,"demand":Demand,"demand_process":DemandProcess,
    "demand_place":DemandPlace,"check_category":CheckCategory,"check_type":CheckType,"check_item": CheckItem,
    "check_output":CheckOutput,"process_estimation":ProcessEstimation,"process_output":ProcessOutput,"script":Script}