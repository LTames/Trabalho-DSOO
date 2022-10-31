class VotacaoIniciadaException(Exception):
    def __init__(self):
        self.msg = 'Impossível alterar cadastros após o início da votação!'
        super().__init__(self.msg)
