from controller.controlador_candidato import ControladorCandidato
from controller.controlador_chapa import ControladorChapa
from controller.controlador_eleitor import ControladorEleitor
from view.tela_urna import TelaUrna


class ControladorUrna():
    def __init__(self) -> None:
        self.__controlador_candidato = ControladorCandidato(self)
        self.__controlador_chapa = ControladorChapa(self)
        self.__controlador_eleitor = ControladorEleitor(self)
        self.__tela_urna = TelaUrna()

    @property
    def controlador_candidato(self):
        return self.__controlador_candidato

    @property
    def controlador_chapa(self):
        return self.__controlador_chapa

    @property
    def controlador_eleitor(self):
        return self.__controlador_eleitor

    @property
    def tela_urna(self):
        return self.__tela_urna

    def cadastra_eleitor(self):
        self.controlador_eleitor.inicia_tela()

    def cadastra_candidato(self):
        pass

    def cadastra_chapa(self):
        pass

    def configura(self):
        pass

    def gera_relatorio_votos(self):
        pass

    def gera_resultado(self):
        pass

    def corrige_utlimo_voto(self):
        pass

    def inclui_eleitor(self):
        pass

    def inclui_votos(self):
        pass

    def inicia_sessao(self):
        self.inicia_tela()

    def encerra_sessao(self):
        pass

    def inicia_tela(self):
        pass
