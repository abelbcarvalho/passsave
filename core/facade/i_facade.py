from abc import ABCMeta
from com.account.model.account import Account


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
