from sqlalchemy.orm import Session
from fastapi import HTTPException
from .repository import Repository
from app.models import models
from app.schemas.produto_schema import Produto


class ProdutoRepositorio(Repository):
  
  def getAll(self, db: Session, skip: int = 0, limit: int = 100):
    getAllProduto = db.query(models.Produto).offset(skip).limit(limit)
    return getAllProduto.all()

  def getById(self, id: str, db:Session) -> Produto:
    pass