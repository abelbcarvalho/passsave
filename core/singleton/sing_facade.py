from core.facade.facade import Facade


class SingFacade:
    """Padrão Singleton para a classe Facade.

    Author:
        abelbcarvalho
    """

    _instance = None

    def __init__(self) -> None:
        """Novo Singleton de Facade.
        """
        pass

    @classmethod
    def facade(cls) -> Facade:
        """Esse metódo verifica a existência
        de Facade instanciada na memória. Se
        não for encontrada, deve ser instanciada.
        Em ambos os casos, a instancia é retornada.

        Returns:
            Facade: instancia de Facade.
        """
        if not cls._instance:
            cls._instance = Facade()
        return cls._instance
