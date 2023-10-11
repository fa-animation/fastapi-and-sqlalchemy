from typing import List
from fastapi import status, APIRouter, Response, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import connect

from app.schemas.schema import Produto
from app.repository import produto_repository

produtolistRepo = produto_repository.ProdutoRepositorio()

router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[Produto])
def getAllProdutos(db: Session = Depends(connect.get_db)):
  """
  GET ALL
  - Listagem de todos produtos
  - Caso não tenha, será retornado uma lista vazia
  """
  return produtolistRepo.getAll(db)
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=Produto)
def getProdutoById(id: int, db: Session = Depends(connect.get_db)):
  """
  GET BY ID
  - Busca um produto pelo id
  - Caso não exista, será retornado um erro
  """
  produtoId = produtolistRepo.getById(id, db)
  if not produtoId:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Produto não encontrado com esse id: {id}")
  return produtoId

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Produto)
def createProduto(produto: Produto, db: Session = Depends(connect.get_db)):
  """
  CREATE
  - Cria um novo produto
  """
  return produtolistRepo.save(produto, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deleteProduto(id: int, db: Session = Depends(connect.get_db)):
  item_content = produtolistRepo.getById(id, db)
  if not item_content:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Produto não encontrado com esse id: {id}")
  produtolistRepo.delete(item_content, db)
  return Response(status_code=status.HTTP_204_NO_CONTENT)