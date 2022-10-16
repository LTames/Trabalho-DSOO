from abc import ABC, abstractmethod


class AbstractTela(ABC):
  
  @abstractmethod
  def exibe_opcoes(self):
    pass