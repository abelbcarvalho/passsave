from core.model.abs_model import AbsModel
from core.data.data import Data


class Info(AbsModel):
    """Classe para informações adicionais
    que porventura sejam necessárias para
    uma conta de login registrada.

    Args:
        AbsModel (Model): chave primária
        e estrangeira.

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """Novo Info.
        """
        super().__init__()
        self._comment = ''
        self._inform = ''
        self._data = Data()

    # getters and setters

    @property
    def comment(self) -> str:
        return self._comment

    @comment.setter
    def comment(self, comment: str) -> None:
        self._comment = comment

    @property
    def inform(self) -> str:
        """Retorna o dado adicional.

        Returns:
            str: dado adicional.
        """
        return self._inform

    @inform.setter
    def inform(self, inform: str) -> None:
        """Insere dado adicional.

        Args:
            inform (str): dado adicional.
        """
        self._inform = inform

    @property
    def data(self) -> Data:
        """Retorna a data.

        Returns:
            Data: instancia de dada.
        """
        return self._data
