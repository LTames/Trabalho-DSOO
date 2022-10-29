from abstracts.abstract_controlador import AbstractControlador
from view.tela_candidato import TelaCandidato
from model.candidato import Candidato, CargoCandidato, TipoEleitor


class ControladorCandidato(AbstractControlador):
    def __init__(self, controlador_urna: 'ControladorUrna') -> None:
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

    def seleciona_candidato(self):
        try:
            num_candidato = self.tela_candidato.get_num_candidato()
            for candidato in self.candidatos:
                if candidato.numero == num_candidato:
                    return candidato
            raise ValueError
        except ValueError:
            self.tela_candidato.alert(
                "Candidato não existente. Verifique seu número e tente novamente")

    def adiciona_candidato(self):
        if len(self.candidatos) == self.controlador_urna.urna.max_eleitores: 
            raise Exception('Número máximo de candidatos atingido!') #new exception

        try:
            dados_candidato = self.tela_candidato.get_dados_candidato()
            for candidato in self.candidatos:
                if dados_candidato["numero"] == candidato.numero:
                    raise ValueError

            dados_candidato["chapa"] = self.controlador_urna.fetch_chapa()

            candidato = Candidato(dados_candidato["cpf"], dados_candidato["nome"], dados_candidato["email"], dados_candidato["endereco"], TipoEleitor(dados_candidato["tipo_eleitor"]), dados_candidato["numero"], dados_candidato["chapa"], CargoCandidato(dados_candidato["cargo"]))

            self.candidatos.append(candidato)
            self.controlador_urna.post_candidato_chapa(candidato)
        except ValueError:
            self.tela_candidato.alert("Candidato já cadastrado com esse número!")

    def deleta_candidato(self) -> None:
        if not self.candidatos:
            self.tela_candidato.alert("Não há candidatos cadastrados")
            return

        candidato = self.seleciona_candidato()
        if not candidato:
            return
        
        self.controlador_urna.delete_candidato_chapa(candidato)
        self.candidatos.remove(candidato)

    def altera_candidato(self) -> None:
        if not self.candidatos:
            self.tela_candidato.alert("Não há candidatos cadastrados")
            return
        candidato = self.seleciona_candidato()
        if not candidato:
            return

        dados_atualizados = self.tela_candidato.get_dados_candidato()
        dados_atualizados["chapa"] = self.controlador_urna.fetch_chapa()
        
        if dados_atualizados["chapa"] != candidato.chapa:
            self.controlador_urna.delete_candidato_chapa(candidato)

        candidato.cpf = dados_atualizados["cpf"]
        candidato.nome = dados_atualizados["nome"]
        candidato.email = dados_atualizados["email"]
        candidato.endereco = dados_atualizados["endereco"]
        candidato.tipo_eleitor = TipoEleitor(dados_atualizados["tipo_eleitor"])
        candidato.numero = dados_atualizados["numero"]
        candidato.chapa = dados_atualizados["chapa"]
        candidato.cargo = CargoCandidato(dados_atualizados["cargo"])

        self.controlador_urna.post_candidato_chapa(candidato)
        

    def lista_candidatos(self) -> None:
        if not self.candidatos:
            self.tela_candidato.alert("Não há candidatos cadastrados")
            return

        for candidato in self.candidatos:
            self.tela_candidato.exibe_candidato({"cpf": candidato.cpf,
                                                 "nome": candidato.nome,
                                                 "email": candidato.email,
                                                 "endereco": candidato.endereco,
                                                 "numero": candidato.numero,
                                                 "chapa": candidato.chapa.nome_chapa,
                                                 "cargo": candidato.cargo.value[1]})

    def inicia_tela(self) -> None:
        acoes = {1: self.altera_candidato, 2: self.adiciona_candidato,
                 3: self.lista_candidatos, 4: self.deleta_candidato, 5: self.retorna}

        while True:
            acoes[self.tela_candidato.exibe_opcoes()]()
