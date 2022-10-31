class MissingEleitoresException(Exception):
    def __init__(self):
        self.msg = 'Antes de votar cadastre o número predefinido de eleitores!'
        super().__init__(self.msg)
