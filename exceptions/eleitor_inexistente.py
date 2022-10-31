class EleitorInexistenteException(Exception):
    def __init__(self):
        self.msg = 'Eleitor não encontrado, verifique seu CPF e tente novamente'
        super().__init__(self.msg)
