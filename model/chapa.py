from model.candidato import Candidato

class Chapa():
    def __init__(self, num_chapa: int, nome_chapa: str, candidatos: list) -> None:
        self.__num_chapa = num_chapa
        self.__nome_chapa = nome_chapa
        self.__candidatos = []
    
    @property
    def num_chapa(self) -> int:
        return self.__num_chapa

    @property
    def nome_chapa(self) -> str:
        return self.__nome_chapa

    @property
    def candidatos(self) -> list:
        return self.__candidatos

    @num_chapa.setter
    def num_chapa(self, num_chapa) -> None:
        self.__num_chapa = num_chapa
    
    @nome_chapa.setter
    def nome_chapa(self, nome_chapa) -> None:
        self.__nome_chapa = nome_chapa
    
    @candidatos.setter
    def candidatos(self, candidatos) -> None:
        self.__candidatos = candidatos