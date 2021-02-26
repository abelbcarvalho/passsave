from core.facade.i_facade import IFacade
from com.account.model.account import Account
from com.account.service.service_account import ServiceAccount
from com.login.model.login import Login
from com.login.service.service_login import ServiceLogin


class Facade(IFacade):
    """Essa é a fachada do projeto, onde
    deve passar o fluxo de dados.

    Args:
        IFacade (interface): interface de facade.

    Author:
        abelbcarvalho
    """

    _serv_acc = ServiceAccount()
    _serv_log = ServiceLogin()

    def __init__(self) -> None:
        """Nova Fachada.
        """
        super().__init__()

    # Account Part

    def create_account(self, account: Account) -> bool:
        """Esse metodo tentará Criar Account.

        Args:
            account (Account): instância com dados
            necessários.

        Returns:
            bool: True se for criado.
        """
        return self._serv_acc.create_account(account=account)

    def read_account(self, **kwargs) -> list:
        """Esse metodo tentará entrar no aplicativo
        com um dicionário como parametro - **kwargs

        Returns:
            list: Account list se encontrado else None.
        """
        return self._serv_acc.read_account(**kwargs)

    def update_account(self, account: Account) -> bool:
        """Esse metodo tentará Atualizar Account.

        Args:
            account (Account): instância com dados
            necessários.

        Returns:
            bool: True se for atualizado.
        """
        return self._serv_acc.update_account(account=account)

    def delete_account(self, account: Account) -> bool:
        """Esse metodo tentará Deletar Account.

        Args:
            account (Account): instância com dados
            necessários.

        Returns:
            bool: True se for deletado.
        """
        return self._serv_acc.delete_account(account=account)

    # Fim Account Part

    # Login Part

    def create_login(self, login: Login) -> bool:
        """Esse metodo tentará Criar Login.

        Args:
            login (Login): instância com dados
            necessários.

        Returns:
            bool: True se for criado.
        """
        return self._serv_log.create_login(login=login)

    def read_login(self, **kwargs) -> list:
        """Esse metodo servirá para realizar
        busca de logins.

        Returns:
            list: lista de Logins ou None.
        """
        return self._serv_log.read_login(**kwargs)

    def update_login(self, login: Login) -> bool:
        """Esse metodo tentará Atualizar Login.

        Args:
            login (Login): instância com dados
            necessários.

        Returns:
            bool: True se for atualizado.
        """
        return self._serv_log.update_login(login=login)

    def delete_login(self, login: Login) -> bool:
        """Esse metodo tentará Deletar Login.

        Args:
            login (Login): instância com dados
            necessários.

        Returns:
            bool: True se for deletado.
        """
        return self._serv_log.delete_login(login=login)

    # Fim Login Part
