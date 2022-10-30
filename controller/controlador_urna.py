from controller.controlador_candidato import ControladorCandidato, CargoCandidato
from controller.controlador_chapa import ControladorChapa
from controller.controlador_eleitor import ControladorEleitor
from model.urna import Urna, Voto
from view.tela_urna import TelaUrna
from abstracts.abstract_controlador import AbstractControlador
from sys import exit
from exceptions.chapa_nao_cadastrada import ChapaNaoCadastradaException
from exceptions.urna_nao_configurada import UrnaNaoConfiguradaException
from exceptions.voto_multiplo import VotoMultiploEXception
from exceptions.candidato_nao_cadastrado import CandidatoNaoCadastradoException


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

    def fetch_eleitor(self, cpf_eleitor: str = None):
        return self.controlador_eleitor.seleciona_eleitor(cpf_eleitor)

    def fetch_candidato(self, num_candidato: int = None, cargo: CargoCandidato = None):
        return self.controlador_candidato.seleciona_candidato(num_candidato, cargo)

    def post_candidato_chapa(self, candidato: 'Candidato'):
        self.controlador_chapa.add_candidato(candidato)

    def delete_candidato_chapa(self, candidato: 'Candidato'):
        self.controlador_chapa.remove_candidato(candidato)

    def vota(self):
        try:
            if not self.urna.configurada:
                raise UrnaNaoConfiguradaException

            if not self.controlador_chapa.chapas:
                raise ChapaNaoCadastradaException

            if not self.controlador_candidato.candidatos:
                raise CandidatoNaoCadastradoException

            eleitor = self.fetch_eleitor()
            if not eleitor:
                return
            if eleitor in self.urna.eleitores:
                raise VotoMultiploEXception
            self.urna.eleitores.append(eleitor) 

            for cargo in CargoCandidato:
                voto = self.tela_urna.get_voto(cargo.value[1])
                
                while True:
                    if voto['confirma'] == 1:
                        if voto['num_candidato'] is not None:
                            candidato = self.fetch_candidato(voto['num_candidato'], cargo)

                            if candidato:
                                self.urna.votos.append(Voto(voto['num_candidato'], cargo))
                            else:
                                self.urna.votos.append(Voto(99, cargo))
                        else:
                            self.urna.votos.append(Voto(0, cargo))
                        break            
                    elif voto['confirma'] == 2:
                        voto = self.tela_urna.get_voto(cargo.value[1])

            self.urna.contador_votos += 1
        except Exception as e:
            self.tela_urna.alert(e)

    def gera_relatorio_votos(self):
        pass

    def gera_resultado(self):
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
            len_eleitores = len(self.controlador_eleitor.eleitores)
            if self.urna.contador_votos == len_eleitores and len_eleitores:
                self.gera_resultado()

            acoes[self.tela_urna.exibe_opcoes()]()
