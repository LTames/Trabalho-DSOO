from controller.controlador_candidato import ControladorCandidato
from controller.controlador_chapa import ControladorChapa
from controller.controlador_eleitor import ControladorEleitor
from model.urna import Urna
from view.tela_urna import TelaUrna


class ControladorUrna():
    def __init__(self) -> None:
        self.__controlador_candidato = ControladorCandidato(self)
        self.__controlador_chapa = ControladorChapa(self)
        self.__controlador_eleitor = ControladorEleitor(self)
        self.__tela_urna = TelaUrna()
        self.__urna = Urna()

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

    @property
    def urna(self):
        return self.__urna

    @urna.setter
    def urna(self, urna: Urna):
        self.__urna = urna

    def configura(self):
        if self.urna.homologada:
            self.tela_urna.alert("Urna já homologada!")
            return

        configuracao = self.tela_urna.get_dados_configuracao()
        self.urna.max_eleitores = configuracao["max_eleitores"]        
        self.urna.max_candidatos = configuracao["max_candidatos"]
        self.urna.turno = configuracao["turno"]
        self.urna.homologada = True

    def cadastra_candidato(self):
        self.controlador_candidato.inicia_tela()
    
    def cadastra_chapa(self):
        self.controlador_chapa.inicia_tela()
    
    def cadastra_eleitor(self):
        self.controlador_eleitor.inicia_tela()

    def vota(self):
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
        acoes = {1: self.configura, 2: self.cadastra_candidato, 3: self.cadastra_chapa, 4: self.cadastra_eleitor, 5: self.vota, 6: self.gera_relatorio_votos}

        while True:
            acoes[self.tela_urna.exibe_opcoes()]()
