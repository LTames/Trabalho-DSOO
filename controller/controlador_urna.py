from logging import exception
from controller.controlador_candidato import ControladorCandidato
from controller.controlador_chapa import ControladorChapa
from controller.controlador_eleitor import ControladorEleitor
from model.urna import Urna
from view.tela_urna import TelaUrna
from abstracts.abstract_controlador import AbstractControlador
from sys import exit
from exceptions.chapa_nao_cadastrada import ChapaNaoCadastradaException
from exceptions.urna_nao_configurada import UrnaNaoConfiguradaException
from exceptions.voto_multiplo import VotoMultiploEXception


class ControladorUrna(AbstractControlador):
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

    def configura(self):
        if self.urna.configurada:
            self.tela_urna.alert("Urna já configurada!")
            return

        configuracao = self.tela_urna.get_dados_configuracao()
        self.urna.max_eleitores = configuracao["max_eleitores"]
        self.urna.max_candidatos = configuracao["max_candidatos"]
        self.urna.turno = configuracao["turno"]
        self.urna.configurada = True

    def cadastra_candidato(self):
        try:
            if not self.controlador_chapa.chapas:
                raise ChapaNaoCadastradaException()
            if not self.urna.configurada:
                raise UrnaNaoConfiguradaException()

            self.controlador_candidato.inicia_tela()
        except Exception as e:
            self.tela_urna.alert(e)

    def cadastra_chapa(self):
        self.controlador_chapa.inicia_tela()

    def cadastra_eleitor(self):
        try:
            if not self.urna.configurada:
                raise UrnaNaoConfiguradaException()

            self.controlador_eleitor.inicia_tela()
        except Exception as e:
            self.tela_urna.alert(e)

    def fetch_chapa(self):
        return self.controlador_chapa.seleciona_chapa()

    def post_candidato_chapa(self, candidato: 'Candidato'):
        self.controlador_chapa.add_candidato(candidato)

    def delete_candidato_chapa(self, candidato: 'Candidato'):
        self.controlador_chapa.remove_candidato(candidato)

    def fetch_eleitor(self):
        return self.controlador_eleitor.seleciona_eleitor()

    def add_eleitor(self):
        eleitor = self.fetch_eleitor()
        try:
            if eleitor in self.urna.eleitores:
                raise VotoMultiploEXception()

            self.urna.eleitores.append(eleitor)
        except Exception as e:
            self.tela_urna.alert(e)

    def vota(self):
        candidatos = self.controlador_candidato.separa_candidatos_por_cargo()
        votos = self.tela_urna.get_dados_votos(candidatos)

    def inclui_votos(self):
        pass

    def gera_relatorio_votos(self):
        pass

    def gera_resultado(self):
        pass

    def corrige_utlimo_voto(self):
        pass

    def inicia_sessao(self):
        self.inicia_tela()

    def inicia_tela(self):
        acoes = {
            1: self.configura,
            2: self.cadastra_candidato,
            3: self.cadastra_chapa,
            4: self.cadastra_eleitor,
            5: self.vota,
            6: self.gera_relatorio_votos,
            7: exit}

        while True:
            acoes[self.tela_urna.exibe_opcoes()]()
