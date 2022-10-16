from urna.abstracts.abstract_tela import AbstractTela


class TelaCandidato(AbstractTela):
  def exibe_opcoes(self):
    print(f'{"=" * 8} Cadastro de Candidato {"=" * 8}')
    print('Escolha uma das opções abaixo')
    print('1 - Alterar Candidato')
    print('2 - Incluir Candidato')
    print('3 - Listar Candidato')
    print('4 - Excluir Candidato')

  def exibe_candidato(self):
    pass

  def get_dados_candidato(self):
    pass

  def get_num_candidato(self):
    pass

TelaCandidato().exibe_opcoes()
