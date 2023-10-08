"""main file where api is started"""
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from app.config.settings import settings
from app.router import users_router
from .database import connect

app = FastAPI(
  title= settings.api_title,
  version= settings.api_version,
  description= settings.api_description,
  contact= {
    "name": settings.api_contact_name,
    "email": settings.api_contact_email
	}
)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
  connect.criar_bd()
  print('Create database')

@app.get("/")
def redirect_docs() -> dict:
  """Redirect to /docs"""
  return RedirectResponse(url='/docs')

app.include_router(users_router.router)