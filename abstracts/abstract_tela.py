from abc import ABC, abstractmethod


class AbstractTela(ABC):

    @abstractmethod
    def exibe_opcoes(self):
        pass

    def alert(self, msg) -> None:
        print(msg)

    def get_int_input(self, input_msg: str, max_int: int = None):
        while True:
            try:
                entrada = int(input(input_msg))

                if max_int:
                    if not (0 < entrada <= max_int):
                        raise ValueError
                    return entrada
                elif entrada < 1:
                    raise ValueError

                return entrada
            except ValueError:
                if max_int:
                    print(
                        f"{'=' * 8} UTILIZE APENAS DÍGITOS ENTRE 1 E {max_int} {'=' * 8}")
                else:
                    print(
                        f"{'=' * 8} UTILIZE APENAS DÍGITOS MAIORES QUE ZERO {'=' * 8}")

    def get_tipo_eleitor(self):
        print('Selecione qual será o tipo de eleitor')
        print('1 - Aluno')
        print('2 - Professor')
        print('3 - Técnico Administrativo')
        return self.get_int_input('Tipo: ', 3)
