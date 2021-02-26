from core.model.abs_model import AbsModel
from core.data.data import Data


class Account(AbsModel):
    """Classe principal que deve ser usada
    para criar uma conta de usuário e poder
    usar o aplicativo.

    Args:
        AbsModel (Model): A chave primária vai
        ser usada.

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """Nova Conta de Usuário.
        """
        super().__init__()
        self._nome = ''
        self._sexo = ''
        self._nasc = Data()
        self._user = ''
        self._email = ''
        self._passw = ''
        self._mobile = ''

    # getters and setters

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome: str) -> None:
        self._nome = nome

    @property
    def sexo(self) -> str:
        return self._sexo

    @sexo.setter
    def sexo(self, sexo: str) -> None:
        self._sexo = sexo

    @property
    def nasc(self) -> Data:
        return self._nasc

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

    @property
    def mobile(self) -> str:
        return self._mobile

    @mobile.setter
    def mobile(self, mobile: str) -> None:
        self._mobile = mobile
