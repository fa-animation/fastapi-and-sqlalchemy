from typing import Union, Optional
from pydantic import BaseModel
from uuid import UUID

class PrudutoBase(BaseModel):
  id: Optional[UUID] = None
  nome: str
  detalhes: Union[str, None] = None
  preco: float
  disponivel: bool
