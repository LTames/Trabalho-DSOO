class Urna():
    def __init__(self):
        self.__votos = []
        self.__eleitores = []
        self.__max_eleitores = None
        self.__max_candidatos = None
        self.__turno = None
        self.__configurada = False

    @property
    def votos(self):
        return self.__votos

    @property
    def eleitores(self):
        return self.__eleitores

    @property
    def max_eleitores(self):
        return self.__max_eleitores

    @property
    def max_candidatos(self):
        return self.__max_candidatos

    @property
    def turno(self):
        return self.__turno

    @property
    def configurada(self):
        return self.__configurada

    @votos.setter
    def votos(self, votos):
        self.__votos = votos

    @eleitores.setter
    def eleitores(self, eleitores):
        self.__eleitores = eleitores

    @max_eleitores.setter
    def max_eleitores(self, max_eleitores):
        self.__max_eleitores = max_eleitores

    @max_candidatos.setter
    def max_candidatos(self, max_candidatos):
        self.__max_candidatos = max_candidatos

    @turno.setter
    def turno(self, turno):
        self.__turno = turno

    @configurada.setter
    def configurada(self, configurada):
        self.__configurada = configurada
