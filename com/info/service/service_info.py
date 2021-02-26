from com.info.model.info import Info
from com.info.service.i_service_info import IServiceInfo
from tools.general import is_none_empty
from tools.general import is_great_than
from tools.name_check import NameCheck
from tools.data_check import DataCheck


class ServiceInfo(IServiceInfo):
    """Regra de negócio para Info.

    Args:
        IServiceInfo (interface): classe
        abstrata que simula interface e
        possuí os metódos para essa classe.

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """Novo Service de Info.
        """
        super().__init__()

    # metodos crud

    def create_info(self, info: Info) -> bool:
        """Esse metodo tentará Criar Info.

        Args:
            info (info): instância com dados
            necessários.

        Returns:
            bool: True se for criado.
        """
        if not isinstance(info, Info):
            return False
        elif not self._checker_create_update(info=info):
            return False

    def read_info(self, **kwargs) -> list:
        """Esse metodo servirá para realizar
        busca de Infos.

        Returns:
            list: lista de Infos ou None.
        """
        if not kwargs:
            return None

    def update_info(self, info: Info) -> bool:
        """Esse metodo tentará Atualizar Info.

        Args:
            info (info): instância com dados
            necessários.

        Returns:
            bool: True se for atualizado.
        """
        if not isinstance(info, Info):
            return False
        elif not info.id > 0:
            return False
        elif not self._checker_create_update(info=info):
            return False

    def delete_info(self, info: Info) -> bool:
        """Esse metodo tentará Deletar Info.

        Args:
            info (info): instância com dados
            necessários.

        Returns:
            bool: True se for deletado.
        """
        if not isinstance(info, Info):
            return False
        elif not info.id > 0:
            return False

    # economizado linhas

    def _checker_create_update(self, info: Info) -> bool:
        """Esse metodo realiza a checagem para criar
        e atualizar, assim economiza linhas de código.

        Args:
            info (Info): Objeto com os dados.

        Returns:
            bool: True se a checagem foi okay.
        """
        if not info.fk > 0:
            return False
        elif is_none_empty(word=info.comment):
            return False
        elif is_none_empty(word=info.inform):
            return False
        elif NameCheck.is_name_okay(word=info.comment):
            return False
        elif is_great_than(word=info.comment, size=60):
            return False
        elif is_great_than(word=info.inform, size=216):
            return False
        elif not DataCheck.is_valid_data(data=info.data):
            return False
        else:
            return True