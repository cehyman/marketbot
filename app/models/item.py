from sqlalchemy import Column, Integer, String, Numeric, Boolean
from sqlalchemy.orm import relationship

from db.base_class import Base



class Items(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    wear = Column(String, index=True)
    max_float = Column(Numeric)
    min_float = Column(Numeric)
    avg_price = Column(Numeric)
    st = Column(Boolean)