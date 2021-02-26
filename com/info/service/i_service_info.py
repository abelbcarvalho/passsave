from abc import ABCMeta
from com.info.model.info import Info


class IServiceInfo(metaclass=ABCMeta):
    """Classe abstrata que simula interface java.
    Deve ser usado como herança em ServiceInfo.

    Author:
        abelbcarvalho
    """

    def create_info(self, info: Info) -> bool:
        pass

    def read_info(self, **kwargs) -> list:
        pass

    def update_info(self, info: Info) -> bool:
        pass

    def delete_info(self, info: Info) -> bool:
        pass
