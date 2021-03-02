from core.facade.i_facade import IFacade
from com.account.model.account import Account
from com.account.service.service_account import ServiceAccount
from com.login.model.login import Login
from com.login.service.service_login import ServiceLogin
from com.info.model.info import Info
from com.info.service.service_info import ServiceInfo
from com.passgen.model.passgen import PassGen
from com.passgen.service.service_passgen import ServicePassGen


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
    _serv_inf = ServiceInfo()
    _serv_pas = ServicePassGen()

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

    def recovery_account(self, account: Account) -> bool:
        """Esse metodo tentará Recuperar Account.
        - passw;
        - user;
        - mobile;

        Args:
            account (Account): instância com dados
            necessários.

        Returns:
            bool: True se for recuperado.
        """
        return self._serv_acc.recovery_account(self, account=account)

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

    def delete_all_login(self, sql='', fk=0) -> bool:
        """Esse metodo tenta deletar todas as contas
        de usuário de uma pessoa no aplicativo.

        Args:
            sql (str, optional): sql query. Defaults to ''.
            fk (int, optional): chave estrangeira. Defaults to 0.

        Returns:
            bool: True se deletado.
        """
        return self._serv_log.delete_all_login(sql=sql, fk=fk)

    # Fim Login Part

    # Info Part

    def create_info(self, info: Info) -> bool:
        """Esse metodo tentará Criar Info.

        Args:
            info (info): instância com dados
            necessários.

        Returns:
            bool: True se for criado.
        """
        return self._serv_inf.create_info(info=info)

    def read_info(self, **kwargs) -> list:
        """Esse metodo servirá para realizar
        busca de Infos.

        Returns:
            list: lista de Infos ou None.
        """
        return self._serv_inf.read_info(**kwargs)

    def update_info(self, info: Info) -> bool:
        """Esse metodo tentará Atualizar Info.

        Args:
            info (info): instância com dados
            necessários.

        Returns:
            bool: True se for atualizado.
        """
        return self._serv_inf.update_info(info=info)

    def delete_info(self, info: Info) -> bool:
        """Esse metodo tentará Deletar Info.

        Args:
            info (info): instância com dados
            necessários.

        Returns:
            bool: True se for deletado.
        """
        return self._serv_inf.delete_info(info=info)

    def delete_all_info(self, sql='', fk=0) -> bool:
        """Esse metodo tenta deletar todas as infos
        de logins de uma pessoa no aplicativo.

        Args:
            sql (str, optional): sql query. Defaults to ''.
            fk (int, optional): chave estrangeira. Defaults to 0.

        Returns:
            bool: True se deletado.
        """
        return self._serv_inf.delete_all_info(sql=sql, fk=fk)

    # Fim Info Part

    # PassGen Part

    def generate_password(self, passgen: PassGen) -> str:
        """Gerar Nova Senha.

        Args:
            passgen (PassGen): Dados para que seja gerada
            a senha.

        Returns:
            str: senha gerada ou None.
        """
        return self._serv_pas.generate_password(passgen=passgen)

    # Fim PassGen Part
