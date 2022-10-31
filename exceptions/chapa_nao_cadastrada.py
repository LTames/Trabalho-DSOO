class ChapaNaoCadastradaException(Exception):
    def __init__(self):
        self.msg = 'Não há chapas cadastradas. Cadastre uma antes de selecionar essa opção!'
        super().__init__(self.msg)
