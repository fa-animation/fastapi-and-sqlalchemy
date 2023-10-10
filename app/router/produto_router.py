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
def users(db: Session = Depends(connect.get_db)):
  """
  GET ALL
  """
  return produtolistRepo.getAll(db)