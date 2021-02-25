from core.connect.connect import Connect
from core.dao.i_dao_base import IDAOBase


class DAOBase(IDAOBase):
    """Fundamentos de DAO, onde os demais
    DAO's devem usar os metódos deste.

    Args:
        IDAOBase (interface): metodos crud.

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """Novo DAOBase.
        """
        super().__init__()

    # metodos crud

    def create(self, sql='', *args) -> bool:
        """Insere dados.

        Args:
            sql (str, optional): sql query. Defaults to ''.

        Returns:
            bool: True se inserido.
        """
        try:
            Connect.open_connection()
            Connect.cursor().execute(sql, args)
            return True
        except Exception as ex:
            print(ex)
            return False
        finally:
            Connect.close_connection()

    def read(self, sql='', *args) -> list:
        """Esse metodo realiza buscas em uma base de dados.

        Args:
            sql (str, optional): sql query. Defaults to ''.

        Returns:
            list: retorna os dados em forma de lista ou None.
        """
        try:
            Connect.open_connection()
            if not args:
                Connect.cursor().execute(sql)
            else:
                Connect.cursor().execute(sql, args)
            return Connect.cursor().fetchall()
        except Exception as ex:
            print(ex)
            return None
        finally:
            Connect.close_connection()

    def update(self, sql='', *args) -> bool:
        """Atualiza dados.

        Args:
            sql (str, optional): sql query. Defaults to ''.

        Returns:
            bool: True se atualizado.
        """
        try:
            Connect.open_connection()
            Connect.cursor().execute(sql, args)
            return True
        except Exception as ex:
            print(ex)
            return False
        finally:
            Connect.close_connection()

    def delete(self, sql='', *args) -> bool:
        """Exclui dados.

        Args:
            sql (str, optional): sql query. Defaults to ''.

        Returns:
            bool: True se excluido.
        """
        try:
            Connect.open_connection()
            Connect.cursor().execute(sql, args)
            return True
        except Exception as ex:
            print(ex)
            return False
        finally:
            Connect.close_connection()
