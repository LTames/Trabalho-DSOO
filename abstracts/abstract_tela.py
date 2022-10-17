from abc import ABC, abstractmethod
from xmlrpc.client import boolean


class AbstractTela(ABC):

    @abstractmethod
    def exibe_opcoes(self):
        pass

    def alert(self, msg) -> None:
        print(msg)

    def get_opcao_escolhida(self, msg: str, nums_validos: list[int]) -> int:
        while True:
            try:
                opcao_selecionada = int(input(msg))
                if not isinstance(opcao_selecionada, int) or not opcao_selecionada in nums_validos:
                    raise ValueError
                return opcao_selecionada
            except ValueError:
                print(f"Utilize apenas dígitos de {nums_validos[0]} a {nums_validos[-1]}!")
