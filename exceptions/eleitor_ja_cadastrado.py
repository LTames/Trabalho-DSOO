class EleitorJaCadastradoException(Exception):
  def __init__(self):
    self.msg = "Eleitor já cadastrado com esse CPF"
    super().__init__(self.msg)
