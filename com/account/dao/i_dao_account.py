from abc import ABCMeta
from com.account.model.account import Account


class IDAOAccount(metaclass=ABCMeta):
    """Classe abstrata que simula interface java.
    Deve ser usado como herança em DAOAccount.

    Author:
        abelbcarvalho
    """

    def create_account(self, account: Account, sql='') -> bool:
        pass

    def read_account(self, **kwargs) -> list:
        pass

    def update_account(self, account: Account, sql='') -> bool:
        pass

    def delete_account(self, account: Account, sql='') -> bool:
        pass
