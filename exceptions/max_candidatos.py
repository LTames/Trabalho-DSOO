class MaxCandidatosException(Exception):
    def __init__(self):
        self.msg = 'Número máximo de candidatos atingido!'
        super().__init__(self.msg)
