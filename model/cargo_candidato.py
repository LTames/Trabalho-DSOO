class CargoCandidato():
    def __init__(self, cargo: str) -> None:
        self.__cargo = cargo

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo
