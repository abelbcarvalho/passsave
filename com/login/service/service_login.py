from com.login.service.i_service_login import IServiceLogin
from tools.data_check import DataCheck
from tools.pass_check import PassCheck
from tools.email_check import EmailCheck
from tools.user_check import UserCheck
from tools.general import is_great_than
from tools.general import is_none_empty
from tools.name_check import NameCheck
from com.login.model.login import Login


class ServiceLogin(IServiceLogin):
    """Regra de negócio para Login.

    Args:
        IServiceLogin (interface): classe
        abstrata que simula interface e
        possuí os metódos para essa classe.

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """Novo Service de Login.
        """
        super().__init__()

    # metodos crud

    def create_login(self, login: Login) -> bool:
        """Esse metodo tentará Criar Login.

        Args:
            login (Login): instância com dados
            necessários.

        Returns:
            bool: True se for criado.
        """
        if not isinstance(login, Login):
            return False
        elif not self._checker_create_update(login=login):
            return False

    def read_login(self, **kwargs) -> list:
        """Esse metodo servirá para realizar
        busca de logins.

        Returns:
            list: lista de Logins ou None.
        """
        if not kwargs:
            return None

    def update_login(self, login: Login) -> bool:
        """Esse metodo tentará Atualizar Login.

        Args:
            login (Login): instância com dados
            necessários.

        Returns:
            bool: True se for atualizado.
        """
        if not isinstance(login, Login):
            return False
        elif not login.id > 0:
            return False
        elif not self._checker_create_update(login=login):
            return False

    def delete_login(self, login: Login) -> bool:
        """Esse metodo tentará Deletar Login.

        Args:
            login (Login): instância com dados
            necessários.

        Returns:
            bool: True se for deletado.
        """
        if not isinstance(login, Login):
            return False
        elif not login.id > 0:
            return False

    def _checker_create_update(self, login: Login) -> bool:
        """Realiza checkagem de create e update.

        Args:
            login (Login): Objeto com os dados.

        Returns:
            bool: True se tudo okay.
        """
        if is_none_empty(word=login.nome):
            return False
        elif not NameCheck.is_name_okay(word=login.nome):
            return False
        elif is_great_than(word=login.nome, size=40):
            return False
        elif is_none_empty(word=login.link):
            return False
        elif is_great_than(word=login.link, size=50):
            return False
        elif not UserCheck.validar_nome_usuario(usuario=login.user):
            return False
        elif not EmailCheck.email_is_valid(email=login.email):
            return False
        elif not PassCheck.verifica_senha_app(senha=login.passw, size=40):
            return False
        elif DataCheck.is_valid_data(data=login.data):
            return False
        elif not login.fk > 0:
            return False
        else:
            return True
