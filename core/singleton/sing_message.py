from core.message.message import Message


class SingMessage:
    """Singleton Pattern para Message.

    Author:
        abelbcarvalho
    """

    _instance = None

    def __init__(self) -> None:
        """Novo Singleton de Message.
        """
        pass

    @classmethod
    def message(cls) -> Message:
        """Verifica existencia de Message,
        se já existir, usa, se não, cria.

        Returns:
            Message: instancia.
        """
        if not cls._instance:
            cls._instance = Message()
        return cls._instance
