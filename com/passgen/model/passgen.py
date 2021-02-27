class PassGen:
    """Classe Modelo para Geração
    de Senhas.

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """Gerar Nova Senha.
        """
        self._numbers = False
        self._upcase = False
        self._lowcase = False
        self._symbol_1 = False
        self._symbol_2 = False
        self._symbol_3 = False
        self._size = 0

    @property
    def numbers(self) -> bool:
        return self._numbers

    @numbers.setter
    def numbers(self, numbers: bool) -> None:
        self._numbers = numbers

    @property
    def upcase(self) -> bool:
        return self._upcase

    @upcase.setter
    def upcase(self, upcase: bool) -> None:
        self._upcase = upcase

    @property
    def lowcase(self) -> bool:
        return self._lowcase

    @lowcase.setter
    def lowcase(self, lowcase: bool) -> None:
        self._lowcase = lowcase

    @property
    def symbol_1(self) -> bool:
        return self._symbol_1

    @symbol_1.setter
    def symbol_1(self, symbol_1: bool) -> None:
        self._symbol_1 = symbol_1

    @property
    def symbol_2(self) -> bool:
        return self._symbol_2

    @symbol_2.setter
    def symbol_2(self, symbol_2: bool) -> None:
        self._symbol_2 = symbol_2

    @property
    def symbol_3(self) -> bool:
        return self._symbol_3

    @symbol_3.setter
    def symbol_3(self, symbol_3: bool) -> None:
        self._symbol_3 = symbol_3

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, size: int) -> None:
        self._size = size
