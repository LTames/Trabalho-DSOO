class ChapaJaCadastradaException(Exception):
    def __init__(self):
        self.msg = "Chapa já cadastrada com esse número!"
        super().__init__(self.msg)
