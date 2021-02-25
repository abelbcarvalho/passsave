class Data:
    """Classe para data de calendário.

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """Nova Data.
        """
        self._dia = 0
        self._mes = 0
        self._ano = 0

    def __str__(self) -> str:
        """Representação da data.

        Returns:
            str: dd/mm/aaaa
        """
        data = ('0' + str(self.dia), str(self.dia))[self.dia > 9]
        data += '/' + ('0' + str(self.mes), str(self.mes))[self.mes > 9]
        data += '/' + str(self.ano)
        return data

    # getters and setters

    @property
    def dia(self) -> int:
        return self._dia

    @dia.setter
    def dia(self, dia: int) -> None:
        self._dia = dia

    @property
    def mes(self) -> int:
        return self._mes

    @mes.setter
    def mes(self, mes: int) -> None:
        self._mes = mes

    @property
    def ano(self) -> int:
        return self._ano

    @ano.setter
    def ano(self, ano: int) -> None:
        self._ano = ano
