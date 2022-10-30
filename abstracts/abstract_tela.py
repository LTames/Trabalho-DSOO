from abc import ABC, abstractmethod


class AbstractTela(ABC):

    @abstractmethod
    def exibe_opcoes(self):
        pass

    def alert(self, msg: str) -> None:
        print(f"{'=' * 8} {msg} {'=' * 8}")

    def get_int_input(self, input_msg: str, max_int: int = None, accept_blank_input: bool = False):
        while True:
            entrada = input(input_msg)
            if accept_blank_input and (not entrada.strip()):
                return None

            try:
                entrada = int(entrada)

                if max_int:
                    if not (0 < entrada <= max_int):
                        raise ValueError
                    return entrada
                elif entrada < 1:
                    raise ValueError

                return entrada
            except ValueError:
                if max_int:
                    self.alert(f"Utilize apenas dígitos entre 1 e {max_int}")
                else:
                    self.alert(f"Utilize apenas dígitos maiores que zero")

    def get_tipo_eleitor(self):
        print('--- Selecione qual será o tipo de eleitor ---')
        print('1 - Aluno')
        print('2 - Professor')
        print('3 - Técnico Administrativo')
        return self.get_int_input('Tipo: ', 3)
