from datetime import datetime
from model.cargo_candidato import CargoCandidato
from model.tipo_eleitor import TipoEleitor


class Voto():
    def __init__(self, num_candidato: int, cargo_candidato: CargoCandidato, tipo_eleitor: TipoEleitor):
        self.__num_candidato = num_candidato
        self.__cargo_candidato = cargo_candidato
        self.__tipo_eleitor = tipo_eleitor
        self.__horario_votacao = datetime.now()

    @property
    def num_candidato(self) -> int:
        return self.__num_candidato

    @num_candidato.setter
    def num_candidato(self, num_candidato) -> None:
        self.__num_candidato = num_candidato

    @property
    def cargo_candidato(self) -> CargoCandidato:
        return self.__cargo_candidato

    @cargo_candidato.setter
    def cargo_candidato(self, cargo_candidato) -> None:
        self.__cargo_candidato = cargo_candidato

    @property
    def tipo_eleitor(self) -> TipoEleitor:
        return self.__tipo_eleitor

    @tipo_eleitor.setter
    def tipo_eleitor(self, tipo_eleitor) -> None:
        self.__tipo_eleitor = tipo_eleitor

    @property
    def horario_votacao(self):
        return self.__horario_votacao

    @horario_votacao.setter
    def horario_votacao(self, horario_votacao) -> None:
        self.__horario_votacao = horario_votacao
