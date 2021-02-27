from abc import ABCMeta
from com.passgen.model.passgen import PassGen


class IServicePassGen(metaclass=ABCMeta):
    """Classe abstrata que simula interface java.
    Deve ser usado como herança em ServicePassGen.

    Author:
        abelbcarvalho
    """

    def generate_password(self, passgen: PassGen) -> str:
        pass
