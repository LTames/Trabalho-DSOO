from abstracts.abstract_controlador import AbstractControlador
from view.tela_chapa import TelaChapa
from model.chapa import Chapa


class ControladorChapa(AbstractControlador):
    def __init__(self, controlador_urna) -> None:
        self.__controlador_urna = controlador_urna
        self.__tela_chapa = TelaChapa()
        self.__chapas = [Chapa(40, "ChapaTeste40"), Chapa(30, "ChapaTeste30")]

    @property
    def controlador_urna(self):
        return self.__controlador_urna

    @property
    def tela_chapa(self) -> TelaChapa:
        return self.__tela_chapa

    @property
    def chapas(self) -> list:
        return self.__chapas

    def adiciona_chapa(self):
        try:
            dados_chapa = self.tela_chapa.get_dados_chapa()
            for candidato in self.candidatos:
                if dados_chapa["numero"] == candidato.numero:
                    raise ValueError

            self.chapas.append(Chapa(dados_chapa["num"],
                                     dados_chapa["nome"],))

        except ValueError:
            self.tela_chapa.alert("Chapa já cadastrada com esse número")

    def deleta_chapa(self) -> None:
        if not self.chapas:
            self.tela_chapa.alert("Não há chapas cadastradas")
            return
        candidato = self.seleciona_chapa(self.tela_chapa.get_num_chapa())
        if not candidato:
            return
        self.candidatos.remove(candidato)

    def altera_chapa(self):
        pass

    def lista_chapas(self):
        pass

    def inicia_tela(self) -> None:
        acoes = {1: self.altera_chapa, 2: self.adiciona_chapa,
                 3: self.lista_chapas, 4: self.deleta_chapa, 5: self.retorna}

        while True:
            acoes[self.tela_chapa.exibe_opcoes()]()
