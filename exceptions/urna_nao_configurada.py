class UrnaNaoConfiguradaException(Exception):
    def __init__(self):
        self.msg = 'Urna não configurada. Realize sua configuração antes de selecionar essa opção!'
        super().__init__(self.msg)
