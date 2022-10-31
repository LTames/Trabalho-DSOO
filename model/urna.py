from model.voto import Voto


class Urna():
    def __init__(self):
        self.__votos = []
        self.__eleitores = []
        self.__max_eleitores = None
        self.__max_candidatos = None
        self.__turno = None
        self.__configurada = False
        self.__contador_votos = 0
        self.__votacao_iniciada = False

    @property
    def votos(self) -> list['Voto']:
        return self.__votos

    @property
    def eleitores(self) -> list['Eleitor']:
        return self.__eleitores

    @property
    def max_eleitores(self) -> int:
        return self.__max_eleitores

    @property
    def max_candidatos(self) -> int:
        return self.__max_candidatos

    @property
    def turno(self) -> int:
        return self.__turno

    @property
    def configurada(self) -> bool:
        return self.__configurada

    @property
    def contador_votos(self) -> int:
        return self.__contador_votos

    @property
    def votacao_iniciada(self) -> bool:
        return self.__votacao_iniciada

    @votos.setter
    def votos(self, votos) -> None:
        self.__votos = votos

    @eleitores.setter
    def eleitores(self, eleitores) -> None:
        self.__eleitores = eleitores

    @max_eleitores.setter
    def max_eleitores(self, max_eleitores) -> None:
        self.__max_eleitores = max_eleitores

    @max_candidatos.setter
    def max_candidatos(self, max_candidatos) -> None:
        self.__max_candidatos = max_candidatos

    @turno.setter
    def turno(self, turno) -> None:
        self.__turno = turno

    @configurada.setter
    def configurada(self, configurada) -> None:
        self.__configurada = configurada

    @contador_votos.setter
    def contador_votos(self, contador_votos) -> None:
        self.__contador_votos = contador_votos

    @votacao_iniciada.setter
    def votacao_iniciada(self, votacao_iniciada) -> None:
        self.__votacao_iniciada = votacao_iniciada
