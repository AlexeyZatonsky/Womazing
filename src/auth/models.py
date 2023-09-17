from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Integer, MetaData, Column, String, UUID, ForeignKey, DateTime, Tuple

from uuid import uuid4
from datetime import datetime



metadata = MetaData()
Base = declarative_base(metadata=metadata)


class User(Base):
    __tablename__ = 'users'

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String)
    mail = Column(String)
    phone = Column(String)
    registrated_at = Column(DateTime, default = datetime.utcnow)