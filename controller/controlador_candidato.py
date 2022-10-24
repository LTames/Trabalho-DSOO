from abstracts.abstract_controlador import AbstractControlador
from view.tela_candidato import TelaCandidato
from model.candidato import Candidato, CargoCandidato, TipoEleitor


class ControladorCandidato(AbstractControlador):
    def __init__(self, controlador_urna) -> None:
        self.__candidatos = []
        self.__tela_candidato = TelaCandidato()
        self.__controlador_urna = controlador_urna

    @property
    def candidatos(self) -> list:
        return self.__candidatos

    @property
    def tela_candidato(self) -> TelaCandidato:
        return self.__tela_candidato

    @property
    def controlador_urna(self):
        return self.__controlador_urna

    def seleciona_candidato(self, numero):
        try:
            for candidato in self.candidatos:
                if candidato.numero == numero:
                    return candidato
            raise ValueError
        except ValueError:
            self.tela_candidato.alert(
                "Candidato não existente. Verifique seu número e tente novamente")

    def adiciona_candidato(self):
        try:
            dados_candidato = self.tela_candidato.get_dados_candidato()
            for candidato in self.candidatos:
                if dados_candidato["numero"] == candidato.numero:
                    raise ValueError

            self.candidatos.append(Candidato(dados_candidato["cpf"],
                                             dados_candidato["nome"],
                                             dados_candidato["email"],
                                             dados_candidato["endereco"],
                                             TipoEleitor(
                                                 dados_candidato["tipo_eleitor"]),
                                             dados_candidato["numero"],
                                             dados_candidato["chapa"],
                                             CargoCandidato(dados_candidato["cargo"])))

        except ValueError:
            self.tela_candidato.alert(
                f"{'=' * 8} CANDIDATO JÁ CADASTRADO COM ESSE NÚMERO {'=' * 8}")

    def deleta_candidato(self) -> None:
        if not self.candidatos:
            self.tela_candidato.alert(
                f"{'=' * 8} NÃO HÁ CANDIDATOS CADASTRADOS {'=' * 8}")
            return

        candidato = self.seleciona_candidato(
            self.tela_candidato.get_num_candidato())
        if not candidato:
            return
        self.candidatos.remove(candidato)

    def altera_candidato(self) -> None:
        if not self.candidatos:
            self.tela_candidato.alert(
                f"{'=' * 8} NÃO HÁ CANDIDATOS CADASTRADOS {'=' * 8}")
            return

        candidato = self.seleciona_candidato(
            self.tela_candidato.get_num_candidato())
        if not candidato:
            return

        dados_atualizados = self.tela_candidato.get_dados_candidato()
        candidato.cpf = dados_atualizados["cpf"]
        candidato.nome = dados_atualizados["nome"]
        candidato.email = dados_atualizados["email"]
        candidato.endereco = dados_atualizados["endereco"]
        candidato.tipo_eleitor = dados_atualizados["tipo_eleitor"]
        candidato.numero = dados_atualizados["numero"]
        candidato.chapa = dados_atualizados["chapa"]
        candidato.cargo = dados_atualizados["cargo"]

    def lista_candidatos(self) -> None:
        if not self.candidatos:
            self.tela_candidato.alert(
                f"{'=' * 8} NÃO HÁ CANDIDATOS CADASTRADOS {'=' * 8}")
            return

        for candidato in self.candidatos:
            self.tela_candidato.exibe_candidato({"cpf": candidato.cpf,
                                                 "nome": candidato.nome,
                                                 "email": candidato.email,
                                                 "endereco": candidato.endereco,
                                                 "numero": candidato.numero,
                                                 "chapa": candidato.chapa,
                                                 "cargo": candidato.cargo})

    def inicia_tela(self) -> None:
        acoes = {1: self.altera_candidato, 2: self.adiciona_candidato,
                 3: self.lista_candidatos, 4: self.deleta_candidato, 5: self.retorna}

        while True:
            acoes[self.tela_candidato.exibe_opcoes()]()
