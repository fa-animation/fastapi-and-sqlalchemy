"""Module Settings"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  """file that loads all env.
  This class contains the following settings:
  * **api_title:** The title of the API.
  * **api_version:** The version of the API.
  * **api_description:** A description of the API.
  * **api_contact_name:** The name of the contact person for the API.
  * **api_contact_email:** The email address of the contact person for the API.

  These settings are loaded from the `.env` file by default.
  """
  api_title: str
  api_version: str
  api_description:str
  api_contact_name:str
  api_contact_email: str

  class Config:
    """Class config fastapi"""
    env_file = ".env"

settings = Settings()
