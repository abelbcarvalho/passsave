from abc import ABCMeta
from com.account.model.account import Account
from com.login.model.login import Login
from com.info.model.info import Info


class IFacade(metaclass=ABCMeta):
    """Classe abstrata que simula o uso
    do recurso de interfaces, nativo do
    java, no python. Deve ser por herança
    em Facade.

    Author:
        abelbcarvalho
    """

    # Account Part

    def create_account(self, account: Account) -> bool:
        pass

    def read_account(self, **kwargs) -> list:
        pass

    def update_account(self, account: Account) -> bool:
        pass

    def delete_account(self, account: Account) -> bool:
        pass

    # Fim de Account

    # Login Part

    def create_login(self, login: Login) -> bool:
        pass

    def read_login(self, **kwargs) -> list:
        pass

    def update_login(self, login: Login) -> bool:
        pass

    def delete_login(self, login: Login) -> bool:
        pass

    # Fim de Login

    # Info Part

    def create_info(self, info: Info) -> bool:
        pass

    def read_info(self, **kwargs) -> list:
        pass

    def update_info(self, info: Info) -> bool:
        pass

    def delete_info(self, info: Info) -> bool:
        pass

    # Fim Info Part
