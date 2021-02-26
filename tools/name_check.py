class NameCheck:
    """Essa classe é responsável pela
    validação de uma palavra, não a
    sintaxe em si, mas seus caracteres.
    [Somente Metodos de Classe.]

    Author:
        abelbcarvalho
    """

    @classmethod
    def is_name_okay(cls, word='') -> bool:
        """Esse metodo tem como principal
        objetivo a realização da verificação
        de um nome, se este pode ser considerado
        válido.

        Args:
            word (str, optional): nome a ser validado. Defaults to ''.

        Returns:
            bool: True se nome for válido.
        """
        if not isinstance(word, str):
            return False
        word = tuple(ord(i) for i in word)
        for i in word:
            if i in cls._gen_special():
                continue
            elif i in cls._gen_lower():
                continue
            elif i in cls._gen_upper():
                continue
            elif i in cls._gen_sym_num():
                continue
            else:
                return False
        else:
            word = ''
            return True

    @classmethod
    def _gen_special(cls):
        """Retorna um gerador de numeros
        ascii para caracteres especiais
        da lingua portuguesa.
        """
        special = (
            192, 193, 194, 195, 199, 201, 202, 205,
            211, 212, 213, 218, 224, 225, 226, 227,
            231, 233, 234, 237, 243, 244, 245, 250,
        )
        return (i for i in special)

    @classmethod
    def _gen_upper(cls):
        """Esse metodo retorna um gerador
        de numeros ascii para caracteres
        letras maiusculas.
        """
        return (i for i in range(65, 91))

    @classmethod
    def _gen_lower(cls):
        """Esse metodo retorna um gerador
        de numeros ascii para caracteres
        letras minusculas.
        """
        return (i for i in range(97, 123))

    @classmethod
    def _gen_sym_num(cls):
        """Esse metodo retorna um gerador de
        caracteres espaço e ponto, assim
        como números.
        """
        special = (32, 46) + tuple(i for i in range(48, 58))
        return (i for i in special)
