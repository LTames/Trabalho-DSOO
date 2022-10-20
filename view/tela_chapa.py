from abstracts.abstract_tela import AbstractTela

class TelaChapa(AbstractTela):
    def exibe_opcoes(self) -> int:
        print(f'{"=" * 8} CADASTRO DE CHAPA {"=" * 8}')
        print('Escolha uma das opções abaixo')
        print('1 - Alterar Chapa')
        print('2 - Incluir Chapa')
        print('3 - Listar Chapa')
        print('4 - Excluir Chapa')
        print('5 - Retornar')

        return self.get_opcao_escolhida("Digite um número: ", [1, 2, 3, 4, 5])
    
    def exibe_chapa(self, dados_chapa: dict) -> None:
        print(f'{"=" * 8} CHAPA: {dados_chapa["nome"]} {"=" * 8}')
        print(f'num: {dados_chapa["num"]}')
        print(f'candidatos: {dados_chapa["candidatos"]}')
    
    def get_dados_chapa(self) -> dict:
        print(f'{"=" * 8} DADOS DA CHAPA {"=" * 8}')
        num = input("Digite o número da chapa: ")
        nome = input("Digite o nome da chapa: ")
        candidatos = input("Digite os candidatos da chapa: ")
       
        return {"num": num,
                "nome": nome,
                "candidatos": candidatos}
