from core.model.abs_model import AbsModel
from core.data.data import Data


class Login(AbsModel):
    """Classe que será responsável por
    guardar os dados e inserir no banco
    de dados, bem como fazer consulta.

    Args:
        AbsModel (Model): recebe a chave primaria 
        e estrangeira.

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """Novo Login.
        """
        super().__init__()
        self._nome = ''
        self._link = ''
        self._user = ''
        self._email = ''
        self._passw = ''
        self._data = Data()

    # getters and setters

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def link(self) -> str:
        return self._link

    @link.setter
    def link(self, link: str) -> None:
        self._link = link

    @property
    def data(self) -> Data:
        return self._data

    @property
    def user(self) -> str:
        return self._user

    @user.setter
    def user(self, user: str) -> None:
        self._user = user

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, email: str) -> None:
        self._email = email

    @property
    def passw(self) -> str:
        return self._passw

    @passw.setter
    def passw(self, passw: str) -> None:
        self._passw = passw
