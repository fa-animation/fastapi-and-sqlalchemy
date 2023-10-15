import uuid
from sqlalchemy import Column, Uuid,String, Float, Boolean
from app.core.database.connect import Base

class Produto(Base):
  __tablename__ = 'produto'

  id = Column(Uuid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
  nome = Column(String)
  detalhes = Column(String)
  preco = Column(Float)
  disponivel = Column(Boolean)