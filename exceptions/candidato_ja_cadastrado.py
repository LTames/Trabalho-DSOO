class CandidatoJaCadastradoException(Exception):
    def __init__(self):
        self.msg = "Candidato já cadastrado com esses dados!"
        super().__init__(self.msg)
