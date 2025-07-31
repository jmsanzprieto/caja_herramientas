from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String, nullable=True)
    price = Column(Integer) # Usamos Integer para simplificar, idealmente usaríamos Numeric
    is_active = Column(Boolean, default=True)