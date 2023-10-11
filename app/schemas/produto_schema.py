from typing import Union, Optional
from pydantic import BaseModel

class Produto(BaseModel):
  """Representa um produto.

  Possui os seguintes atributos:

  * **id:** O identificador do produto. Este atributo é opcional.
  * **nome:** O nome do produto. Este atributo é obrigatório.
  * **descricao:** A descrição do produto. Este atributo é opcional.
  * **valor:** O valor do produto. Este atributo é obrigatório.  
  """
  id: Optional[str] = None
  nome: str
  detalhe: Union[str, None] = None
  preco: float
  disponivel: bool
  class Config:
    orm_mode = True
  
class UpdateProduto(BaseModel):
  nome: Optional[str]
  descricao: Optional[str]
  valor: Optional[float]
  class Config:
    orm_mode = True