from abc import ABCMeta
from com.login.model.login import Login


class IDAOLogin(metaclass=ABCMeta):
    """Classe abstrata que simula interface java.
    Deve ser usado como herança em DAOLogin.

    Author:
        abelbcarvalho
    """

    def create_login(self, login: Login, sql='') -> bool:
        pass

    def read_login(self, **kwargs) -> list:
        pass

    def update_login(self, login: Login, sql='') -> bool:
        pass

    def delete_login(self, login: Login, sql='') -> bool:
        pass

    def delete_all_login(self, sql='', fk=0) -> bool:
        pass
