from fastapi import status, APIRouter, Request

router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK)
def users():
  """
  GET ALL
  """
  return {"message": "Hello World"}
