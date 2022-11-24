from sqlalchemy import Column,Integer,String,ForeignKey
from config import Base


class Process(Base):
    __tablename__ = "process"

    process_id = Column(Integer,primary_key=True,autoincrement=True)
    fk_unit_category = Column(Integer,ForeignKey("unit_category.unit_category_id",ondelete="CASCADE"),nullable=False)
    fk_unit = Column(Integer,ForeignKey("unit.unit_id",ondelete="CASCADE"),nullable=False)
    fk_unit_position = Column(Integer,ForeignKey("unit_position.unit_position_id",ondelete="CASCADE"),nullable=False)
    fk_demand_category = Column(Integer,ForeignKey("demand_category.demand_category_id",ondelete="CASCADE"),nullable=False)
    fk_demand_type = Column(Integer,ForeignKey("demand_type.demand_type_id",ondelete="CASCADE"),nullable=False)
    fk_demand = Column(Integer, ForeignKey("demand.demand_id",ondelete="CASCADE"),nullable=False)
    fk_demand_process = Column(Integer,ForeignKey("demand_process.demand_process_id",ondelete="CASCADE"),nullable=False)
    fk_demand_place = Column(Integer,ForeignKey("demand_place.demand_place_id",ondelete="CASCADE"),nullable=False)
    fk_check_category = Column(Integer,ForeignKey("check_category.check_category_id",ondelete="CASCADE"),nullable=False)
    fk_check_type = Column(Integer,ForeignKey("check_type.check_type_id",ondelete="CASCADE"),nullable=False)
    fk_check_item = Column(Integer,ForeignKey("check_item.check_item_id",ondelete="CASCADE"),nullable=False)
    fk_check_output = Column(Integer,ForeignKey("check_output.check_output_id",ondelete="CASCADE"),nullable=False)
    fk_process_estimation = Column(Integer,ForeignKey("process_estimation.process_estimation_id",ondelete="CASCADE"),nullable=False)
    fk_process_output = Column(Integer,ForeignKey("process_output.process_output_id",ondelete="CASCADE"),nullable=False)
    fk_script = Column(Integer,ForeignKey("script.script_id",ondelete="CASCADE"),nullable=False)
    #fk_pointer_process = Column(Integer,ForeignKey("pointer_process.id",ondelete="CASCADE"))




"""class PointerProcess(Base):
__tablename__ = "pointer_process"

id =column(Integer,primary=True)
fk_process = column(Integer,ForeignKey("process.id",ondelete="CASCADE"))
fk_pointer_process = column(Integer,ForeignKey("process.pointer_process_id",ondelete="CASCADE"))

"""

