from abc import ABC, abstractmethod

class Repository(ABC):

  @abstractmethod
  def getAll(self, skip: int = 0, limit: int = 100):
      pass
  @abstractmethod
  def getById(self, id: int):
      pass
  @abstractmethod
  def save(self, model):
      pass