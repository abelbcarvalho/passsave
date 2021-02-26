from tools.general import is_none_empty, take_space
from tools.general import make_str_list_each, is_small_equal


class EmailCheck:
    """
    Classe para validação de endereço de e-mail.
    [Somente com Metodos de Classe.]

    Author:
        abelbcarvalho
    """

    # metodo principal

    @classmethod
    def email_is_valid(cls, email='') -> bool:
        """Metodo que trabalha na validação de um email.

        Args:
            email (str): endereço de e-mail a ser testado.

        Returns:
            bool: True se o email for válido.
        """
        if is_none_empty(email):
            return False
        elif not isinstance(email, str):
            return False
        # tirando espaços
        email = take_space(email)
        if not is_small_equal(email, 256):
            return False
        elif not cls._only_one_at(make_str_list_each(email)):
            return False
        elif email[0].__eq__('@') or email[-1].__eq__('@'):
            return False
        elif not email[0].isalpha() or not email[-1].isalpha():
            return False
        elif not cls._near_at_alpha_numeric(email):
            return False
        elif not cls._char_valid(email):
            return False
        else:
            return True

    # caracteres válidos teste

    @classmethod
    def _only_one_at(cls, lista: list) -> bool:
        """Esse metodo checa se existe apenas
        uma '@' numa lista.

        Args:
            lista (list): email transformado em list.

        Returns:
            bool: True se existir apenas um '@'.
        """
        return lista.count('@') == 1

    @classmethod
    def _near_at_alpha_numeric(cls, email='') -> bool:
        """Metodo que verifica se imediato antes ou depois de um '@'
        o caractere é alfanumérico.

        Args:
            email (str, optional): endereço de email. Defaults to ''.

        Returns:
            bool: True se imediato antes e depois de @ é alfanumérico.
        """
        index = email.index('@')
        if not email[index-1].isalpha() and not email[index-1].isnumeric():
            return False
        elif not email[index+1].isalpha() and not email[index+1].isnumeric():
            return False
        return True

    @classmethod
    def _char_valid(cls, email='') -> bool:
        """Metodo que verifica se os caracteres de um
        email são validos.

        Args:
            email (str, optional): endereço de e-mail. Defaults to ''.

        Returns:
            bool: True se todos os caracteres de um endereço
            de e-mail, são considerados válidos.
        """
        validos = ('@', '.', '_',)
        numeros = (chr(a) for a in range(48, 58))
        letras = (chr(a) for a in range(97, 123))
        for a in numeros:
            validos += tuple(a, )
        for a in letras:
            validos += tuple(a, )
        numeros = None
        index = email.index('@')
        letras = [a for a in email[index+1:]]
        if letras.__len__() < 1:
            return False
        letras = None
        aux = make_str_list_each(email)
        return cls._email_char_valids(chaves=validos, valores=tuple(aux))

    @classmethod
    def _email_char_valids(cls, chaves=(), valores=()) -> bool:
        """Essa classe verifica se o email tem caracteres válidos.
        (depende de _char_valid())

        Args:
            chaves (tuple, optional): chaves para os valores. Defaults to ().
            valores (tuple, optional): valores. Defaults to ().

        Returns:
            bool: True se o e-mail só tem válidos caracteres.
        """
        tem = True
        for val in valores:
            if not tem:
                return False
            tem = False
            for cha in chaves:
                if val == cha:
                    tem = True
                    break
        return True
