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

    def seleciona_eleitor(self, cpf: str = None):
        try:
            if not cpf:
                cpf = self.tela_eleitor.get_cpf_eleitor()
            for eleitor in self.eleitores:
                if eleitor.cpf == cpf:
                    return eleitor
            raise ValueError
        except ValueError:
            self.tela_eleitor.alert(
                "Eleitor não existente. Verifique seu cpf e tente novamente")
    
    def adiciona_eleitor(self):
        try:
            dados_eleitor = self.tela_eleitor.get_dados_eleitor()
            for eleitor in self.eleitores:
                if dados_eleitor["cpf"] == eleitor.cpf:
                    raise ValueError

            self.eleitores.append(Eleitor(dados_eleitor["cpf"],
                                          dados_eleitor["nome"],
                                          dados_eleitor["email"],
                                          dados_eleitor["endereco"],
                                          dados_eleitor["tipo_eleitor"]))

        except ValueError:
            self.tela_eleitor.alert("Eleitor já cadastrado com esse CPF")

    def deleta_eleitor(self):
        if not self.eleitores:
            self.tela_eleitor.alert("Não há eleitores cadastrados")
            return
        eleitor = self.seleciona_eleitor(self.tela_eleitor.get_cpf_eleitor())
        if not eleitor:
            return
        self.eleitores.remove(eleitor)
    
    def altera_eleitor(self):
        if not self.eleitores:
            self.tela_eleitor.alert('Não há eleitores cadastrados')
            return
        eleitor = self.seleciona_eleitor(self.tela_eleitor.get_cpf_eleitor())
        if not eleitor:
            return
        
        dados_atualizados = self.tela_eleitor.get_cpf_eleitor()
        eleitor.cpf = dados_atualizados["cpf"]
        eleitor.nome = dados_atualizados["nome"]
        eleitor.email = dados_atualizados["email"]
        eleitor.endereco = dados_atualizados["endereco"]
        eleitor.tipo_eleitor = dados_atualizados["tipo_eleitor"]

    def lista_eleitores(self):
        if not self.eleitores:
            self.tela_eleitor.alert('Não há eleitores cadastrados')
            return
        for eleitor in self.eleitores:
            self.tela_eleitor.exibe_eleitor({'cpf': eleitor.cpf, 'nome': eleitor.nome,
                                             'email': eleitor.email, 'endereco': eleitor.endereco,
                                             'tipo_eleitor': eleitor.tipo_eleitor})

    def inicia_tela(self) -> None:
        acoes = {1: self.altera_eleitor, 2: self.adiciona_eleitor,
                 3: self.lista_eleitores, 4: self.deleta_eleitor, 5: self.retorna}

        while True:
            acoes[self.tela_eleitor.exibe_opcoes()]()
