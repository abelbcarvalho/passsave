from com.account.model.account import Account
from com.account.service.i_service_account import IServiceAccount


class ServiceAccount(IServiceAccount):
    """Regra de negócio para Account.

    Args:
        IServiceAccount (interface): classe
        abstrata que simula interface e
        possuí os metódos para essa classe.

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """Novo Service de Account.
        """
        super().__init__()

    # metodos crud

    def create_account(self, account: Account) -> bool:
        """Esse metodo tentará Criar Account.

        Args:
            account (Account): instância com dados
            necessários.

        Returns:
            bool: True se for criado.
        """
        pass

    def read_account(self, **kwargs) -> list:
        """Esse metodo tentará entrar no aplicativo
        com um dicionário como parametro - **kwargs

        Returns:
            list: Account list se encontrado else None.
        """
        pass

    def update_account(self, account: Account) -> bool:
        """Esse metodo tentará Atualizar Account.

        Args:
            account (Account): instância com dados
            necessários.

        Returns:
            bool: True se for atualizado.
        """
        pass

    def delete_account(self, account: Account) -> bool:
        """Esse metodo tentará Deletar Account.

        Args:
            account (Account): instância com dados
            necessários.

        Returns:
            bool: True se for deletado.
        """
        pass
