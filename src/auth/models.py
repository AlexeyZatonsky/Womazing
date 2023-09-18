from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Integer, MetaData, Column, String, UUID, ForeignKey, TIMESTAMP, Boolean
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID


from uuid import uuid4
from datetime import datetime



metadata = MetaData()
Base = declarative_base(metadata=metadata)


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    first_name = Column(String)
    lust_name = Column(String)
    email = Column(String)
    phone = Column(String)
    registrated_at = Column(TIMESTAMP, default = datetime.utcnow)
    hashed_password = Column(String(length=1024))
    is_active = Column(Boolean)
    is_superuser = Column(Boolean)
    is_verified = Column(Boolean)
