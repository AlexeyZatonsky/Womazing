from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, MetaData, ForeignKey, Integer, String, UUID

from uuid import uuid4

from ..store.models import Store



metadata = MetaData()
Base = declarative_base(metadata=metadata)


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)




class Product(Base):
    __tablename__ = "products"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String)
    category_id = Column(Integer, ForeignKey(Category.id))
    store_id = Column(Integer, ForeignKey(Store.id))
