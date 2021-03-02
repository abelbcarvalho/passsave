from abc import ABCMeta
from com.account.model.account import Account


class IServiceAccount(metaclass=ABCMeta):
    """Classe abstrata que simula interface java.
    Deve ser usado como herança em ServiceAccount.

    Author:
        abelbcarvalho
    """

    def create_account(self, account: Account) -> bool:
        pass

    def read_account(self, **kwargs) -> list:
        pass

    def update_account(self, account: Account) -> bool:
        pass

    def delete_account(self, account: Account) -> bool:
        pass

    def recovery_account(self, account: Account) -> bool:
        pass
