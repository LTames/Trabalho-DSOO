from datetime import datetime
from cargo_candidato import CargoCandidato


class Voto():
    def __init__(self, num_candidato: int, cargo_candidato: CargoCandidato):
        self.__num_candidato = num_candidato
        self.__cargo_candidato = cargo_candidato
        self.__horario_votacao = datetime.now()

    @property
    def num_candidato(self) -> int:
        return self.__num_candidato

    @num_candidato.setter
    def num_candidato(self, num_candidato) -> None:
        self.__num_candidato = num_candidato

    @property
    def horario_votacao(self):
        return self.__horario_votacao

    @horario_votacao.setter
    def horario_votacao(self, horario_votacao):
        self.__horario_votacao = horario_votacao

    @property
    def cargo_candidato(self):
        return self.__cargo_candidato

    @cargo_candidato.setter
    def cargo_candidato(self, cargo_candidato):
        self.__cargo_candidato = cargo_candidato
