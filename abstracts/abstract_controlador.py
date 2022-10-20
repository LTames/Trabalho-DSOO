from abc import ABC, abstractmethod


class AbstractControlador(ABC):

    @abstractmethod
    def inicia_tela(self):
        pass

    def retorna(self) -> None:
        self.controlador_urna.inicia_tela()
