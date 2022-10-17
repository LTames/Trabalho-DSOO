from abstracts.abstract_tela import AbstractTela

class TelaEleitor(AbstractTela):
    pass

    def exibe_opcoes(self) -> int:
        print(f'{"=" * 8} CADASTRO DE ELEITOR {"=" * 8}')
        print('Escolha uma das opções abaixo')
        print('1 - Alterar Eleitor')
        print('2 - Incluir Eleitor')
        print('3 - Listar Eleitor')
        print('4 - Excluir Eleitor')
        print('5 - Retornar')
        
        return self.get_opcao_escolhida("Digite um número: ", [1, 2, 3, 4, 5])
    
    def exibe_eleitor(self, dados_eleitor: dict) -> None:
        print(f'{"=" * 8} ELEITOR: {dados_eleitor["nome"]} {"=" * 8}')
        print(f'CPF: {dados_eleitor["cpf"]}')
        print(f'E-MAIL: {dados_eleitor["email"]}')
        print(f'ENDEREÇO: {dados_eleitor["endereco"]}')
        print(f'TIPO: {dados_eleitor["tipo"]}')