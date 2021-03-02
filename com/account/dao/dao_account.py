from com.account.model.account import Account
from com.account.dao.i_dao_account import IDAOAccount
from core.dao.dao_base import DAOBase


class DAOAccount(IDAOAccount):
    """Esse é o dao de Account. Aqui é possível
    realizar as operações referentes a Banco
    de Dados.

    Args:
        IDAOAccount (interface): possui os metodos de account.

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """Novo DAO de Account.
        """
        super().__init__()
        self._dao = DAOBase()

    def create_account(self, account: Account, sql='') -> bool:
        """Esse metodo tenta Inserir Account.

        Args:
            account (Account): Modelo com dados.
            sql (str, optional): sql query. Defaults to ''.

        Returns:
            bool: True se inserido.
        """
        return self._dao.create(
            sql,
            account.nome, account.sexo, account.nasc.dia,
            account.nasc.mes, account.nasc.ano, account.user,
            account.email, account.passw, account.mobile,
        )

    def read_account(self, **kwargs) -> list:
        """Esse metódo tenta verificar a existencia
        de Account com base nos dados enviados.

        Returns:
            list: lista não nula se encontrado.
        """
        return self._dao.read(
            kwargs['sql'],
            kwargs['user'],
            kwargs['email'],
            kwargs['passw']
        )

    def update_account(self, account: Account, sql='') -> bool:
        """Esse metodo tenta Atualizar Account.

        Args:
            account (Account): Modelo com dados.
            sql (str, optional): sql query. Defaults to ''.

        Returns:
            bool: True se atualizado.
        """
        return self._dao.update(
            sql,
            account.nome, account.sexo, account.nasc.dia,
            account.nasc.mes, account.nasc.ano, account.user,
            account.email, account.passw, account.mobile,
            account.id
        )

    def delete_account(self, account: Account, sql='') -> bool:
        """Esse metodo tenta Deletar Account.

        Args:
            account (Account): Modelo com dados.
            sql (str, optional): sql query. Defaults to ''.

        Returns:
            bool: True se deletado.
        """
        return self._dao.delete(sql, account.id)

    def thare_are_email_or_user(self, sql='', *args) -> list:
        """Esse metodo verifica se existe email or user
        já registrado.

        Args:
            sql (str, optional): sql query. Defaults to ''.

        Returns:
            list: lista de id or None.
        """
        return self._dao.read(sql, args)
