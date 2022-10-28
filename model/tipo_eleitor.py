from enum import Enum


class TipoEleitor(Enum):
    ALUNO = (1, "Aluno")
    PROFESSOR = (2, "Professor")
    TECNICO_ADMINISTRATIVO = (3, "Técnico Administrativo")

    @classmethod
    def _missing_(cls, valor):
        for tipo in cls:
            if tipo.value[0] == valor:
                return tipo
