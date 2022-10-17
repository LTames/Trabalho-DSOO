from abstracts.abstract_tela import AbstractTela


class TelaCandidato(AbstractTela):
    def exibe_opcoes(self) -> int:
        print(f'{"=" * 8} Cadastro de Candidato {"=" * 8}')
        print('Escolha uma das opções abaixo')
        print('1 - Alterar Candidato')
        print('2 - Incluir Candidato')
        print('3 - Listar Candidato')
        print('4 - Excluir Candidato')
        print('5 - Retornar')

        opcao_selecionada = int(input("Digite a opção: "))
        return opcao_selecionada

    def exibe_candidato(self, dados_candidato: dict) -> None:
        print(f'CPF: {dados_candidato["cpf"]}')
        print(f'NOME: {dados_candidato["nome"]}')
        print(f'E-MAIL: {dados_candidato["email"]}')
        print(f'ENDEREÇO: {dados_candidato["endereco"]}')
        print(f'NÚMERO: {dados_candidato["numero"]}')
        print(f'CHAPA: {dados_candidato["chapa"]}')
        print(f'CARGO: {dados_candidato["cargo"]}')

    def get_dados_candidato(self) -> dict:
        cpf_candidato = input("Digite o CPF do candidato: ")
        nome_candidato = input("Digite o nome do candidato: ")
        email_candidato = input("Digite o e-mail do candidato: ")
        endereco_candidato = input("Digite o endereço do candidato: ")
        # tipo_eleitor
        numero_candidato = int(input("Digite o número do candidato: "))
        # chapa
        # cargo

        return {"cpf": cpf_candidato,
                "nome": nome_candidato,
                "email": email_candidato,
                "endereco": endereco_candidato,
                "tipo_eleitor": tipo_eleitor,
                "numero": numero_candidato,
                "chapa": chapa,
                "cargo": cargo}

    def get_num_candidato(self) -> int:
        num = int(input("Digite o número do candidato: "))
        return num


