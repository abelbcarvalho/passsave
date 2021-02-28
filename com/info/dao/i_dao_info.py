from abc import ABCMeta
from com.info.model.info import Info


class IDAOInfo(metaclass=ABCMeta):
    """Classe abstrata que simula interface java.
    Deve ser usado como herança em DAOinfo.

    Author:
        abelbcarvalho
    """

    def create_info(self, info: Info, sql='') -> bool:
        pass

    def read_info(self, **kwargs) -> list:
        pass

    def update_info(self, info: Info, sql='') -> bool:
        pass

    def delete_info(self, info: Info, sql='') -> bool:
        pass

    def delete_all_info(self, sql='', fk=0) -> bool:
        pass
