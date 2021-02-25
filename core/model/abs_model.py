from abc import ABCMeta


class AbsModel(metaclass=ABCMeta):
    """Classe abstrata que funciona como
    modelo inicial de uma entidade de
    banco de dados. Nela se encontram as
    refêrencias para a chave primária
    e a chave estrangeira (se necessário).

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """Novo Modelo Abstrato.
        """
        self._id = 0
        self._fk = 0

    # getters and setters

    @property
    def id(self) -> int:
        """Retorna a Chave Primária.

        Returns:
            int: a chave primária.
        """
        return self._id

    @id.setter
    def id(self, id: int) -> None:
        """Insere a Chave Primária.

        Args:
            id (int): Chave Primária.
        """
        self._id = id

    @property
    def fk(self) -> int:
        """Retorna a Chave Estrangeira.

        Returns:
            int: a chave estrangeira.
        """
        return self._fk

    @fk.setter
    def fk(self, fk: int) -> None:
        """Insere a Chave Estrangeira.

        Args:
            fk (int): Chave estangeira.
        """
        self._fk = fk
