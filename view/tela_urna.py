from abstracts.abstract_tela import AbstractTela


class TelaUrna(AbstractTela):
    def exibe_opcoes(self):
        print(f'--- Eleições 2022 ---')
        print('Escolha uma das opções abaixo')
        print('1 - Configurar Urna')
        print('2 - Cadastrar Candidato')
        print('3 - Cadastrar Chapa')
        print('4 - Cadastrar Eleitor')
        print('5 - Votar')
        print('6 - Gerar Relatório dos Votos')
        print('7 - Encerrar Sessão')

        opcao = self.get_int_input("Digite a opção: ", 7)
        return opcao

    def exibe_relatorio(self, dados_relatorio: dict):
        def exibe_votos(cargo: str, cargo_display: str):
            for num_candidato, votos in dados_relatorio[cargo].items():
                print(f'===== {cargo_display.title()} =====')
                print(f'N° Candidato: {num_candidato} | Alunos: {votos["aluno"]} | Professores: {votos["professor"]} | Técnicos Administrativos: {votos["tecnico_administrativo"]}')
                print('')

        print('--- Relatório Preliminar Eleições 2022 ---')
        exibe_votos('reitor', 'Reitor')
        exibe_votos('pro_reitor_extensao', 'Pró-Reitor de Extensão')
        exibe_votos('pro_reitor_graduacao', 'Pró-Reitor de Graduação')
        exibe_votos('pro_reitor_pesquisa', 'Pró-Reitor de Pesquisa')
        print(f"Brancos: {dados_relatorio['brancos']} | Nulos: {dados_relatorio['nulos']} | Total de Votos: {dados_relatorio['num_votos']}")

    def exibe_resultado(self, dados_resultado):
        pass

    def get_dados_configuracao(self):
        print(f'--- Configuração da Urna ---')
        max_eleitores = self.get_int_input(
            "Digite o número máximo de eleitores: ")
        max_candidatos = self.get_int_input(
            "Digite o número máximo de candidatos: ")
        turno = self.get_int_input("Digite o turno da eleição: ", 2)

        return {"max_eleitores": max_eleitores,
                "max_candidatos": max_candidatos, "turno": turno}

    def get_voto(self, cargo: str):
        print(f'Vote para o candidato a {cargo}')
        num_candidato = self.get_int_input(f'Número do candidato: ', 98, True)
        
        print('1 - Sim')
        print('2 - Corrige')
        confirma = self.get_int_input('Confirma ?: ', 2)

        return {'num_candidato': num_candidato, 'confirma': confirma}
