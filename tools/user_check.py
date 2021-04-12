from tools.general import is_none_empty
from tools.general import is_great_than
from tools.general import take_space
from tools.general import make_str_list_each


class UserCheck:
    """
    Verificador de nome de usuário.
    [Somente com Metodos de Classe.]

    Author:
        abelbcarvalho
    """

    # metodo principal

    @classmethod
    def validar_nome_usuario(cls, usuario='', size=32) -> bool:
        """Esse metodo tentará validar um nome de usuário.

        Args:
            usuario (str, optional): [description]. Defaults to ''.
            size (int, optional): tamanho. Defaults to 32.

        Returns:
            bool: True se o nome de usuario for válido.
        """
        if is_none_empty(word=usuario):
            return False
        elif is_great_than(word=usuario, size=size):
            return False
        usuario = take_space(word=usuario)
        usuario = tuple(make_str_list_each(word=usuario), )
        validos = cls._generate_valid_char()
        return cls._is_valid_username_text(validos=validos, usuario=usuario)

    @classmethod
    def _generate_valid_char(cls) -> tuple:
        """Esse metodo gera uma tupla com todos
        os caracteres válidos.

        Returns:
            tuple: tupla de caracteres válidos.
        """
        simbolos = (chr(num) for num in range(45, 47))
        numeros = (chr(num) for num in range(48, 58))
        letras_1 = (chr(num) for num in range(97, 123))
        todos = ()
        for num in simbolos:
            todos += (num, )
        for num in numeros:
            todos += (num, )
        for num in letras_1:
            todos += (num, )
        return todos + ('_', )

    @classmethod
    def _is_valid_username_text(cls, validos=(), usuario=()) -> bool:
        """Esse metodo verifica se uma tupla tem os elementos
        contidos em outra.

        Args:
            validos (tuple, optional): caracteres válidos. Defaults to ().
            usuario (tuple, optional): nome de usuário em tupla. Defaults to ().

        Returns:
            bool: True se todos os caracteres são válidos.
        """
        tem = True
        for a in usuario:
            if not tem:
                return False
            tem = False
            for b in validos:
                if a == b:
                    tem = True
                    break
        else:
            return True
