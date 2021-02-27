from abc import ABCMeta
from com.passgen.model.passgen import PassGen


class IPassMaker(metaclass=ABCMeta):
    """Classe abstrata que simula interface java.
    Deve ser usado como herança em PassMaker.

    Author:
        abelbcarvalho
    """

    def generate_password(self, passgen: PassGen) -> str:
        pass

    def _gen_numbers(self, allow: bool):
        pass

    def _gen_upper(self, allow: bool):
        pass

    def _gen_lower(self, allow: bool):
        pass

    def _gen_symbol_1(self, allow: bool):
        pass

    def _gen_symbol_2(self, allow: bool):
        pass

    def _gen_symbol_3(self, allow: bool):
        pass
