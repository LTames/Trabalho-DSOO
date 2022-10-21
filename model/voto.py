class Voto():
    def __init__(self, num_candidato):
        self.__num_candidato = num_candidato

    @property
    def num_candidato(self):
        return self.__num_candidato

    @num_candidato.setter
    def num_candidato(self, num_candidato):
        self.__num_candidato = num_candidato
