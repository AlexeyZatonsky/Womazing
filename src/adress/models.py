from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import UUID, ForeignKey, MetaData, Column, Integer, String

from auth.models import User



metadata = MetaData()
Base = declarative_base(metadata=metadata)


class Adress(Base):
    __tablename__ = "adresses"

    id = Column(Integer, primary_key=True)
    country = Column(String)
    city = Column(String)
    street = Column(String)
    number = Column(String)
    user_uuid = Column(UUID, ForeignKey(User.id))

