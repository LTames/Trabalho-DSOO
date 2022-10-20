from abc import ABC, abstractmethod
from xmlrpc.client import boolean


class AbstractTela(ABC):

    @abstractmethod
    def exibe_opcoes(self):
        pass

    def alert(self, msg) -> None:
        print(msg)

    # def get_opcao_escolhida(self, input_msg: str, nums_validos: list[int]) -> int:
    #     while True:
    #         try:
    #             opcao_selecionada = int(input(input_msg))
    #             if not (opcao_selecionada in nums_validos):
    #                 raise ValueError
    #             return opcao_selecionada
    #         except ValueError:
    #             print(f"{'=' * 8} UTILIZE APENAS DÍGITOS DE {nums_validos[0]} A {nums_validos[-1]}! {'=' * 8}")

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
                    print(f"{'=' * 8} UTILIZE APENAS DÍGITOS ENTRE 1 E {max_int} {'=' * 8}")
                else:
                    print(f"{'=' * 8} UTILIZE APENAS DÍGITOS MAIORES QUE ZERO {'=' * 8}")
