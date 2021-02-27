from com.login.model.login import Login
from com.login.dao.i_dao_login import IDAOLogin
from core.dao.dao_base import DAOBase


class DAOLogin(IDAOLogin):
    """Esse é o dao de Login. Aqui é possível
    realizar as operações referentes a Banco
    de Dados.

    Args:
        IDAOLogin (interface): possui os metodos de login.

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """Novo DAO de Login.
        """
        super().__init__()
        self._dao = DAOBase()

    def create_login(self, login: Login, sql='') -> bool:
        """Esse metodo tenta Inserir login.

        Args:
            login (Login): Modelo com dados.
            sql (str, optional): sql query. Defaults to ''.

        Returns:
            bool: True se inserido.
        """
        return self._dao.create(
            sql,
            login.nome,login.link,login.user,
            login.email,login.passw,login.data.dia,
            login.data.mes,login.data.ano,login.fk
        )

    def read_login(self, **kwargs) -> list:
        """Esse metódo tenta verificar a existencia
        de Login com base nos dados enviados.

        Returns:
            list: lista não nula se encontrado.
        """
        data = tuple(kwargs[i] for i in kwargs if i != 'sql')
        return self._dao.read(kwargs['sql'], data)

    def update_login(self, login: Login, sql='') -> bool:
        """Esse metodo tenta Atualizar Login.

        Args:
            login (Login): Modelo com dados.
            sql (str, optional): sql query. Defaults to ''.

        Returns:
            bool: True se atualizado.
        """
        return self._dao.update(
            sql,
            login.nome,login.link,login.user,
            login.email,login.passw,login.data.dia,
            login.data.mes,login.data.ano,login.fk,
            login.id,
        )

    def delete_login(self, login: Login, sql='') -> bool:
        """Esse metodo tenta Deletar Login.

        Args:
            login (Login): Modelo com dados.
            sql (str, optional): sql query. Defaults to ''.

        Returns:
            bool: True se deletado.
        """
        return self._dao.delete(sql, login.id)

    def delete_all_login(self, sql='', fk=0) -> bool:
        """Esse metodo tenta deletar todas as contas
        de usuário de uma pessoa no aplicativo.

        Args:
            sql (str, optional): sql query. Defaults to ''.
            fk (int, optional): chave estrangeira. Defaults to 0.

        Returns:
            bool: True se deletado.
        """
        return self._dao.delete(sql, fk)
