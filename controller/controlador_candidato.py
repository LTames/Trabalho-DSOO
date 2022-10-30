from abstracts.abstract_controlador import AbstractControlador
from view.tela_candidato import TelaCandidato
from model.candidato import Candidato, CargoCandidato, TipoEleitor
from exceptions.max_candidatos import MaxCandidatosException
from exceptions.candidato_ja_cadastrado import CandidatoJaCadastradoException
from exceptions.candidato_inexistente import CandidatoInexistenteException


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

    def seleciona_candidato(self, num_candidato: int = None, cargo: CargoCandidato = None):
        try:
            if not num_candidato:
                num_candidato = self.tela_candidato.get_num_candidato()
            for candidato in self.candidatos:
                if cargo is not None:
                    if candidato.numero == num_candidato and candidato.cargo == cargo:
                        return candidato
                elif candidato.numero == num_candidato:
                    return candidato
            raise CandidatoInexistenteException
        except Exception as e:
            self.tela_candidato.alert(e)

    def adiciona_candidato(self):
        if len(self.candidatos) == self.controlador_urna.urna.max_candidatos: 
            raise MaxCandidatosException

        try:
            dados_candidato = self.tela_candidato.get_dados_candidato()
            for candidato in self.candidatos:
                if dados_candidato["numero"] == candidato.numero or dados_candidato['cpf'] == candidato.cpf:
                    raise CandidatoJaCadastradoException

            dados_candidato["chapa"] = self.controlador_urna.fetch_chapa()

            candidato = Candidato(dados_candidato["cpf"], dados_candidato["nome"], dados_candidato["email"], dados_candidato["endereco"], TipoEleitor(dados_candidato["tipo_eleitor"]), dados_candidato["numero"], dados_candidato["chapa"], CargoCandidato(dados_candidato["cargo"]))

            self.controlador_urna.post_candidato_chapa(candidato)
            self.controlador_urna.post_candidato_eleitores(candidato)
            self.candidatos.append(candidato)
        except Exception as e:
            self.tela_candidato.alert(e)

    def deleta_candidato(self) -> None:
        if not self.candidatos:
            self.tela_candidato.alert("Não há candidatos cadastrados")
            return

        candidato = self.seleciona_candidato()
        if not candidato:
            return
        
        self.controlador_urna.delete_candidato_chapa(candidato)
        self.controlador_urna.delete_candidato_eleitores(candidato)
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

    def separa_candidatos_por_cargo(self):
        reitores = []
        pro_reitores_extensao = []
        pro_reitores_graduacao = []
        pro_reitores_pesquisa = []
        
        for candidato in self.candidatos:
            dados_candidato = {'nome': candidato.nome, 'numero': candidato.numero}
            
            match candidato.cargo:
                case CargoCandidato.REITOR:
                    reitores.append(dados_candidato)
                case CargoCandidato.PRO_REITOR_EXTENSAO:
                    pro_reitores_extensao.append(dados_candidato)
                case CargoCandidato.PRO_REITOR_GRADUACAO:
                    pro_reitores_graduacao.append(dados_candidato)                
                case CargoCandidato.PRO_REITOR_PESQUISA:
                    pro_reitores_pesquisa.append(dados_candidato)

        return {'reitor': reitores, 'pro_reitor_extensao': pro_reitores_extensao, 'pro_reitor_graduacao': pro_reitores_graduacao, 'pro_reitor_pesquisa': pro_reitores_pesquisa}

    def inicia_tela(self) -> None:
        acoes = {1: self.altera_candidato, 2: self.adiciona_candidato,
                 3: self.lista_candidatos, 4: self.deleta_candidato, 5: self.retorna}

        while True:
            acoes[self.tela_candidato.exibe_opcoes()]()
