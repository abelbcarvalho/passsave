from tools.general import is_none_empty
from tools.general import is_equals
from tools.general import make_str_list
from tools.general import str_can_int_float


class MobileCheck:
    """
    Essa Classe trabalha com a validação de números
    de celular. [Somente com Metodos de Classe.]

    Author:
        abelbcarvalho
    """

    # metodo principal

    @classmethod
    def mobile_valid(cls, mobile='', size=14) -> bool:
        """Esse metodo valida um número de telefone quanto a
        caracteres inválido. Basta que seja enviado o numero
        de telefone em str, e se desejar, o tamanho em int.
        Por default, o valor do tamanho é 14. O número deve
        começar com '+'.

        Args:
            mobile (str, optional): número de celular. Defaults to ''.
            size (int, optional): número de caracteres. Defaults to 14.

        Returns:
            bool: True se o numero de celular for válido.
        """
        if is_none_empty(mobile):
            return False
        elif not is_equals(mobile, size):
            return False
        elif not mobile[0].__eq__('+'):
            return False
        else:
            return cls._is_valid_mobile(tuple(make_str_list(mobile)))

    @classmethod
    def _is_valid_mobile(cls, numeros=()) -> bool:
        """Percorre a tupla e compara os elementos.
        Verifica se todos os caracteres configuram
        em um número de telefone válido.

        Args:
            numeros (tuple): Número de telefone em
            forma de tupla.

        Returns:
            bool: True se o numero de telefone for válido.
        """
        for num in numeros[1:]:
            try:
                if not str_can_int_float(word=str(num)):
                    return False
                elif not num.isnumeric():
                    return False
            except AttributeError:
                return False
        else:
            return True
