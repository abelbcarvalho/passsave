from abc import ABCMeta
from com.login.model.login import Login


class IServiceLogin(metaclass=ABCMeta):
    """Classe abstrata que simula interface java.
    Deve ser usado como herança em ServiceLogin.

    Author:
        abelbcarvalho
    """

    def create_login(self, login: Login) -> bool:
        pass

    def read_login(self, **kwargs) -> list:
        pass

    def update_login(self, login: Login) -> bool:
        pass

    def delete_login(self, login: Login) -> bool:
        pass
