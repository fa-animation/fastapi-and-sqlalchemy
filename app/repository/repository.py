from abc import ABC, abstractmethod

class Repository(ABC):

  @abstractmethod
  def getAll(self, skip: int = 0, limit: int = 100):
      pass