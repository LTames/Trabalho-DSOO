from abstracts.abstract_tela import AbstractTela


class TelaChapa(AbstractTela):
    def exibe_opcoes(self) -> int:
        print(f'{"=" * 8} CADASTRO DE CHAPA {"=" * 8}')
        print('Escolha uma das opções abaixo')
        print('1 - Alterar Chapa')
        print('2 - Incluir Chapa')
        print('3 - Listar Chapas')
        print('4 - Excluir Chapa')
        print('5 - Retornar')

        return self.get_int_input("Digite um número: ", 5)

    def exibe_chapa(self, dados_chapa: dict) -> None:
        print(f'{"=" * 8} CHAPA: {dados_chapa["nome_chapa"]} {"=" * 8}')
        print(f'num_chapa: {dados_chapa["num_chapa"]}')
        
    def get_dados_chapa(self) -> dict:
        print(f'{"=" * 8} DADOS DA CHAPA {"=" * 8}')
        num_chapa = input("Digite o número da chapa: ")
        nome_chapa = input("Digite o nome da chapa: ")

        return {"num_chapa": num_chapa,
                "nome_chapa": nome_chapa}

    def get_num_chapa(self) -> int:
        num_chapa = self.get_int_input("Digite o número da chapa: ")
        return num_chapa
