from typing import Union, Optional
from pydantic import BaseModel

class PrudutoBase(BaseModel):
  id: Optional[int] = None
  nome: str
  detalhes: Union[str, None] = None
  preco: float
  disponivel: bool
