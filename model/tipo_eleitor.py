from enum import Enum


class TipoEleitor(Enum):
    ALUNO = (1, "Aluno")
    PROFESSOR = (2, "Professor")
    TECNICO_ADMINISTRATIVO = (3, "Técnico Administrativo")
