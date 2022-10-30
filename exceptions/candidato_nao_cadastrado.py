class CandidatoNaoCadastradoException(Exception):
  def __init__(self):
    self.msg = 'Não há candidatos cadastrados. Cadastre um candidato antes de selecionar essa opção!'
    super().__init__(self.msg)
