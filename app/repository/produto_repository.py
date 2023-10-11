from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .repository import Repository
from sqlalchemy.exc import IntegrityError
from app.models import models
from app.schemas.schema import Produto


class ProdutoRepositorio(Repository):
  
  def getAll(self, db: Session, skip: int = 0, limit: int = 100):
    getAllProduto = db.query(models.Produto).offset(skip).limit(limit)
    return getAllProduto.all()

  def getById(self, id: int, db:Session) -> Produto:
    return db.query(models.Produto).filter(models.Produto.id == id).first()
  
  def save(self, produto, db: Session):
    produto_db = models.Produto(**produto.dict())
    try:
      db.add(produto_db)
      db.commit()
      db.refresh(produto_db)
      return produto_db
    except IntegrityError as err:
      db.rollback()
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{err}" )
    
  def delete(self, item_content, db: Session):
    db.delete(item_content)
    db.commit()
    return item_content