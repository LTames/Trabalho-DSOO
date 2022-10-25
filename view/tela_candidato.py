from abstracts.abstract_tela import AbstractTela


class TelaCandidato(AbstractTela):
    def exibe_opcoes(self) -> int:
        print(f'{"=" * 8} CADASTRO DE CANDIDATO {"=" * 8}')
        print('Escolha uma das opções abaixo')
        print('1 - Alterar Candidato')
        print('2 - Incluir Candidato')
        print('3 - Listar Candidatos')
        print('4 - Excluir Candidato')
        print('5 - Retornar')

        return self.get_int_input("Digite a opção: ", 5)

    def exibe_candidato(self, dados_candidato: dict) -> None:
        print(f'{"=" * 8} CANDIDATO: {dados_candidato["nome"]} {"=" * 8}')
        print(f'CPF: {dados_candidato["cpf"]}')
        print(f'E-MAIL: {dados_candidato["email"]}')
        print(f'ENDEREÇO: {dados_candidato["endereco"]}')
        print(f'NÚMERO: {dados_candidato["numero"]}')
        print(f'CHAPA: {dados_candidato["chapa"]}')
        print(f'CARGO: {dados_candidato["cargo"]}')

    def get_dados_candidato(self, chapas_cadastradas: list) -> dict:
        print(f'{"=" * 8} DADOS DO CANDIDATO {"=" * 8}')
        cpf_candidato = input("Digite o CPF do candidato: ")
        nome_candidato = input("Digite o nome do candidato: ")
        email_candidato = input("Digite o e-mail do candidato: ")
        endereco_candidato = input("Digite o endereço do candidato: ")
        numero_candidato = self.get_int_input(
            "Digite o número do candidato: ", 98)

        tipo_eleitor = self.get_tipo_eleitor()
        chapa = self.get_chapa(chapas_cadastradas)
        cargo = self.get_cargo_candidato()

        return {"cpf": cpf_candidato,
                "nome": nome_candidato,
                "email": email_candidato,
                "endereco": endereco_candidato,
                "numero": numero_candidato,
                "tipo_eleitor": tipo_eleitor,
                "chapa": chapa,
                "cargo": cargo}

    def get_num_candidato(self) -> int:
        num = self.get_int_input("Digite o número do candidato: ")
        return num

    def get_cargo_candidato(self) -> int:
        print('--- Selecione o cargo no qual o candidato irá concorrer ---')
        print('1 - Reitor')
        print('2 - Pró Reitor (Graduação)')
        print('3 - Pró Reitor (Pesquisa)')
        print('4 - Pró Reitor (Extensão)')
        return self.get_int_input('Cargo: ', 4)

    def get_chapa(self, chapas: list) -> int:
        print('Selecione a atual chapa do candidato')
        for i, chapa in enumerate(chapas):
            print(f'{i + 1} - {chapa.nome_chapa} ({chapa.num_chapa})')

        return self.get_int_input('Chapa: ', len(chapas)) - 1
