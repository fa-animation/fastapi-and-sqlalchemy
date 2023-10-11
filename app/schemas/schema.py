from .base import base_model_schema

class Produto(base_model_schema.PrudutoBase):
  class Config:
    from_attributes = True
    json_schema_extra = {
        "example": {
          "id": 1,
          "nome": "Maçã",
          "detalhes": "maçã de boa qualidade",
          "preco": 2.40,
          "disponivel": True
      }
    }
