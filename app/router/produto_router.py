from typing import List
from sqlalchemy.orm import Session
from app.database import connect
from fastapi import status, APIRouter, HTTPException, Depends

from app.schemas.produto_schema import Produto
from app.repository import produto_repository

produtolistRepo = produto_repository.ProdutoRepositorio()

router = APIRouter(
  prefix="/produto",
  tags=["produto"],
)

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[Produto])
def getAllProdutos(db: Session = Depends(connect.get_db)):
  """
  GET ALL
  """
  return produtolistRepo.getAll(db)
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=Produto)
def getProdutoById(id: str, db: Session = Depends(connect.get_db)):
  """
  GET ONE
  """
  produtoId = produtolistRepo.getById(id, db)
  if not produtoId:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Produto não encontrado com esse id: {id}")
  return produtoId