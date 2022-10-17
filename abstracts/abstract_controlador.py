from abc import ABC, abstractmethod


class AbstractControlador(ABC):

    @abstractmethod
    def inicia_tela(self):
        pass
