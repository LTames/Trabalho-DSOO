class MissingCandidatosException(Exception):
  def __init__(self):
    self.msg = 'Antes de votar cadastre o número predefinido de candidatos!'
    super().__init__(self.msg)
