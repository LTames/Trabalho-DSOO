class CandidatoInexistenteException(Exception):
  def __init__(self):
    self.msg = 'Candidato não encontrado'
    super().__init__(self.msg)
