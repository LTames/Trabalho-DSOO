from abc import ABC, abstractmethod


class AbstractControlador(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def inicia_tela(self):
        pass

    def retorna(self) -> None:
        self.controlador_urna.inicia_tela()
