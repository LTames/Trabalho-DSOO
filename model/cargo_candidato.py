from enum import Enum


class CargoCandidato(Enum):
    REITOR = (1, "Reitor")
    PRO_REITOR_GRADUACAO = (2, "Pró-Reitor de Graduação")
    PRO_REITOR_PESQUISA = (3, "Pró-Reitor de Pesquisa")
    PRO_REITOR_EXTENSAO = (4, "Pró-Reitor de Extensão")

    @classmethod
    def _missing_(cls, valor):
        for cargo in cls:
            if cargo.value[0] == valor:
                return cargo
