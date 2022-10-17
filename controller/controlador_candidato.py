from abstracts.abstract_controlador import AbstractControlador
from view.tela_candidato import TelaCandidato
from model.candidato import Candidato

class ControladorCandidato(AbstractControlador):
    def __init__(self, controlador_urna) -> None:
        self.__candidatos = []
        self.__tela_candidato = TelaCandidato()
        self.__controlador_urna = controlador_urna

    @property
    def candidatos(self):
        return self.__candidatos
    
    @property
    def tela_candidato(self):
        return self.__tela_candidato
    
    @property
    def controlador_urna(self):
        return self.__controlador_urna

    def seleciona_candidato(self, numero):
        while True:
            try:
                for candidato in self.candidatos:
                    if candidato.numero == numero:
                        return candidato
                raise ValueError
            except:
                print("Candidato não existente. Verifique seu número e tente novamente")
                numero = self.tela_candidato.get_num_candidato()

    def adiciona_candidato(self):
        dados_candidato = self.tela_candidato.get_dados_candidato()
        self.candidatos.append(Candidato(dados_candidato["cpf"],
                                         dados_candidato["nome"],
                                         dados_candidato["email"],
                                         dados_candidato["endereco"],
                                         dados_candidato["tipo_eleitor"],
                                         dados_candidato["numero"],
                                         dados_candidato["chapa"],
                                         dados_candidato["cargo"]))

    def deleta_candidato(self):
        candidato = self.seleciona_candidato(self.tela_candidato.get_num_candidato())
        self.candidatos.remove(candidato)

    def altera_candidato(self):
        candidato = self.seleciona_candidato(self.tela_candidato.get_num_candidato())

    def lista_candidatos(self):
        for candidato in self.candidatos:
            self.tela_candidato.exibe_candidato({"cpf": candidato.cpf,
                                                 "nome": candidato.nome,
                                                 "email": candidato.email,
                                                 "endereco": candidato.endereco,
                                                 "numero": candidato.numero,
                                                 "chapa": candidato.chapa,
                                                 "cargo": candidato.cargo})

    def retorna(self):
        self.controlador_urna.inicia_tela()

    def inicia_tela(self):
        pass
