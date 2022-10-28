class Voto():
    def __init__(self, num_candidato):
        self.__num_candidato = num_candidato

    @property
    def num_candidato(self) -> int:
        return self.__num_candidato

    @num_candidato.setter
    def num_candidato(self, num_candidato) -> None:
        self.__num_candidato = num_candidato
