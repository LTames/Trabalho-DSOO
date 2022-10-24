from abstracts.abstract_controlador import AbstractControlador
from view.tela_chapa import TelaChapa
from model.chapa import Chapa


class ControladorChapa(AbstractControlador):
    def __init__(self, controlador_urna) -> None:
        self.__controlador_urna = controlador_urna
        self.__tela_chapa = TelaChapa()
        self.__chapas = []

    @property
    def controlador_urna(self):
        return self.controlador_urna

    @property
    def tela_chapa(self) -> TelaChapa:
        return self.tela_chapa

    @property
    def chapas(self) -> list:
        return self.chapas

    def adiciona_chapa(self):
        try:
            dados_chapa = self.tela_chapa.get_dados_chapa()
            for candidato in self.candidatos:
                if dados_chapa["numero"] == candidato.numero:
                    raise ValueError

            self.chapas.append(Chapa(dados_chapa["num"],
                                     dados_chapa["nome"],
                                     dados_chapa["candidatos"]))

        except ValueError:
            self.tela_chapa.alert(
                f"{'=' * 8} CHAPA JÁ CADASTRADA COM ESSE NÚMERO {'=' * 8}")

    def deleta_chapa(self) -> None:
        if not self.chapas:
            self.tela_chapa.alert(
                f"{'=' * 8} NÃO HÁ CHAPAS CADASTRADAS {'=' * 8}")
            return
        candidato = self.seleciona_chapa(self.tela_chapa.get_num_chapa())
        if not candidato:
            return
        self.candidatos.remove(candidato)

    def inicia_tela(self):
        pass
