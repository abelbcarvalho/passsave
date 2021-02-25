from abc import ABCMeta


class IDAOBase(metaclass=ABCMeta):
    """Classe que simula uma interface
    java no python. trata-se de uma
    classe abstrata que deve ser por
    herança na classe DAOBase, neste
    pacote.

    Author:
        abelbcarvalho
    """

    def create(self, sql='', *args) -> bool:
        pass

    def read(self, sql='', *args) -> list:
        pass

    def update(self, sql='', *args) -> bool:
        pass

    def delete(self, sql='', *args) -> bool:
        pass
