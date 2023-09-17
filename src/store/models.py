from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, MetaData, Integer, String




metadata = MetaData()
Base = declarative_base(metadata=metadata)


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
