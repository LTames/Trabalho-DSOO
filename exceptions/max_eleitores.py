class MaxEleitoresException(Exception):
  def __init__(self):
    self.msg = 'Número máximo de eleitores atingido!'
    super().__init__(self.msg)
