from abstracts.abstract_tela import AbstractTela


class TelaEleitor(AbstractTela):
    def exibe_opcoes(self) -> int:
        print(f'--- CADASTRO DE ELEITOR ---')
        print('Escolha uma das opções abaixo')
        print('1 - Alterar Eleitor')
        print('2 - Incluir Eleitor')
        print('3 - Listar Eleitor')
        print('4 - Excluir Eleitor')
        print('5 - Retornar')

        return self.get_int_input("Digite um número: ", 5)

    def exibe_eleitor(self, dados_eleitor: dict) -> None:
        print(f'--- ELEITOR: {dados_eleitor["nome"]} ---')
        print(f'CPF: {dados_eleitor["cpf"]}')
        print(f'E-MAIL: {dados_eleitor["email"]}')
        print(f'ENDEREÇO: {dados_eleitor["endereco"]}')
        print(f'TIPO: {dados_eleitor["tipo_eleitor"]}')

    def get_dados_eleitor(self) -> dict:
        print(f'--- DADOS DO ELEITOR ---')
        cpf_eleitor = int(input("Digite o CPF do eleitor: "))
        nome_eleitor = input("Digite o nome do eleitor: ")
        email_eleitor = input("Digite o e-mail do eleitor: ")
        endereco_eleitor = input("Digite o endereço do eleitor: ")
        # tipo_eleitor

        return {"cpf": cpf_eleitor,
                "nome": nome_eleitor,
                "email": email_eleitor,
                "endereco": endereco_eleitor,
                "tipo_eleitor": None}

    def get_cpf_eleitor(self) -> int:
        cpf = self.get_int_input("Digite o cpf do eleitor: ")
        return cpf