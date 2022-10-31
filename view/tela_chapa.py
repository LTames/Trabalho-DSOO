from abstracts.abstract_tela import AbstractTela


class TelaChapa(AbstractTela):
    def exibe_opcoes(self) -> int:
        print(f'--- CADASTRO DE CHAPA ---')
        print('Escolha uma das opções abaixo')
        print('1 - Alterar Chapa')
        print('2 - Incluir Chapa')
        print('3 - Listar Chapas')
        print('4 - Excluir Chapa')
        print('5 - Retornar')

        return self.get_int_input("Digite um número: ", 5)

    def exibe_chapa(self, dados_chapa: dict) -> None:
        print(f'--- CHAPA: {dados_chapa["nome_chapa"]} ---')
        print(f'NÚMERO DA CHAPA: {dados_chapa["num_chapa"]}')
        print(
            f"CANDIDATOS: {', '.join([candidato.nome.title() for candidato in dados_chapa['candidatos']])}")

    def get_dados_chapa(self) -> dict:
        print(f'--- DADOS DA CHAPA ---')
        num_chapa = self.get_int_input("Digite o número da chapa: ", 99)
        nome_chapa = input("Digite o nome da chapa: ")

        return {"num_chapa": num_chapa,
                "nome_chapa": nome_chapa}

    def get_chapa(self, chapas) -> int:
        print(f'Escolha sua chapa')
        for i in range(len(chapas)):
            print(f'{i+1}: {chapas[i].nome_chapa} ({chapas[i].num_chapa})')
        indice_chapa = self.get_int_input("Digite a sua opcão: ", len(chapas))
        return indice_chapa - 1
