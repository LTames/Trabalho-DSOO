class VotoMultiploEXception(Exception):
    def __init__(self):
        self.msg = 'Voto já confirmado com esse CPF. Impossível continuar!'
        super().__init__(self.msg)
