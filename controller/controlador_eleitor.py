from abstracts.abstract_controlador import AbstractControlador
from view.tela_eleitor import TelaEleitor
from model.eleitor import Eleitor


class ControladorEleitor(AbstractControlador):
    def __init__(self, controlador_urna) -> None:
        self.__controlador_urna = controlador_urna
        self.__tela_eleitor = TelaEleitor()
        self.__eleitores = []

    @property
    def controlador_urna(self):
        return self.__controlador_urna

    @property
    def tela_eleitor(self) -> TelaEleitor:
        return self.__tela_eleitor

    @property
    def eleitores(self) -> list:
        return self.__eleitores

    def adiciona_eleitor(self):
        try:
            dados_eleitor = self.tela_eleitor.get_dados_eleitor()
            for eleitor in self.eleitores:
                if dados_eleitor["numero"] == eleitor.cpf:
                    raise ValueError

            self.eleitores.append(Eleitor(dados_eleitor["cpf"],
                                          dados_eleitor["nome"],
                                          dados_eleitor["email"],
                                          dados_eleitor["endereco"],
                                          dados_eleitor["tipo_eleitor"]))

        except ValueError:
            self.tela_eleitor.alert("Eleitor já cadastrado com esse CPF")

    def deleta_eleitor(self):
        pass

    def altera_eleitor(self):
        pass

    def lista_eleitores(self):
        pass

    def inicia_tela(self) -> None:
        acoes = {1: self.altera_eleitor, 2: self.adiciona_eleitor,
                 3: self.lista_eleitores, 4: self.deleta_eleitor, 5: self.retorna}

        while True:
            acoes[self.tela_eleitor.exibe_opcoes()]()
