from com.info.model.info import Info
from com.info.dao.i_dao_info import IDAOInfo
from core.dao.dao_base import DAOBase


class DAOInfo(IDAOInfo):
    """Esse é o dao de Info. Aqui é possível
    realizar as operações referentes a Banco
    de Dados.

    Args:
        IDAOinfo (interface): possui os metodos de Info.

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """Novo DAO de Info.
        """
        super().__init__()
        self._dao = DAOBase()

    def create_info(self, info: Info, sql='') -> bool:
        """Esse metodo tenta Inserir Info.

        Args:
            info (Info): Modelo com dados.
            sql (str, optional): sql query. Defaults to ''.

        Returns:
            bool: True se inserido.
        """
        return self._dao.create(
            sql,
            info.comment,info.inform,
            info.data.dia,info.data.mes,
            info.data.ano,info.fk
        )

    def read_info(self, **kwargs) -> list:
        """Esse metódo tenta verificar a existencia
        de Info com base nos dados enviados.

        Returns:
            list: lista não nula se encontrado.
        """
        data = tuple(kwargs[i] for i in kwargs if i != 'sql')
        return self._dao.read(kwargs['sql'], data) if data \
            else self._dao.read(kwargs['sql'])

    def update_info(self, info: Info, sql='') -> bool:
        """Esse metodo tenta Atualizar Info.

        Args:
            info (Info): Modelo com dados.
            sql (str, optional): sql query. Defaults to ''.

        Returns:
            bool: True se atualizado.
        """
        return self._dao.update(
            sql,
            info.comment,info.inform,info.data.dia,
            info.data.mes,info.data.ano,info.fk,
            info.id,
        )

    def delete_info(self, info: Info, sql='') -> bool:
        """Esse metodo tenta Deletar Info.

        Args:
            info (Info): Modelo com dados.
            sql (str, optional): sql query. Defaults to ''.

        Returns:
            bool: True se deletado.
        """
        return self._dao.delete(sql, info.id)

    def delete_all_info(self, sql='', fk=0) -> bool:
        """Esse metodo tenta deletar todas as infos
        de logins de uma pessoa no aplicativo.

        Args:
            sql (str, optional): sql query. Defaults to ''.
            fk (int, optional): chave estrangeira. Defaults to 0.

        Returns:
            bool: True se deletado.
        """
        return self._dao.delete(sql, fk)
