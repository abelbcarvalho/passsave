class Encript:
    """Classe com metodos pronto para encriptar e
    desemcriptar. Todos são metodos de classe.
    * Utilize:
    - encript;
    - decript;

    Author:
        abelbcarvalho
    """

    def __init__(self):
        """New instance of Encript class.
        """
        pass

    @classmethod
    def encript(cls, word='', passw=''):
        """
        This method is for encrypt a word with a password to go back
        to original.

        Args:
            word (str, optional): word to encript. Defaults to ''.
            passw (str, optional): password of encriptation. Defaults to ''.

        Returns:
            str: encripted word or None.
        """
        if not word or not passw:
            return None
        elif passw.__len__() < 3:
            return None
        elif word.__len__() > 40:
            return None
        elif passw.__len__() > 40:
            return None
        # mix sty
        word = cls._mix_strs(str1=word, str2=passw)
        passw = None
        # become tuple
        word = cls._str_tuple(str1=word)
        # reverse
        word = cls._reverse_tuple(tuple1=word)
        # to ascii int
        word = cls._tuple_ascii_int(tuple1=word)
        # change values
        word = cls._change_int(tuple1=word)
        # to ascii str
        word = cls._tuple_ascii_str(tuple1=word)
        # add equals
        word = cls._add_equals(tuple1=word)
        # tuple in str
        return cls._tuple_str(tuple1=word)

    @classmethod
    def decript(cls, word='', passw=''):
        """
        This method is for decrypt a word with a password to go back
        to original.

        Args:
            word (str, optional): word to encript. Defaults to ''.
            passw (str, optional): password of encriptation. Defaults to ''.

        Returns:
            str: original word or None.
        """
        if not word or not passw:
            return None
        elif passw.__len__() < 3:
            return None
        elif word.__len__() > 82:
            return None
        elif passw.__len__() > 40:
            return None
        # delete equals
        word = cls._delete_equals(str1=word)
        # str in tuple
        word = cls._str_tuple(str1=word)
        # ascii int
        word = cls._tuple_ascii_int(tuple1=word)
        # revert int
        word = cls._revert_int(tuple1=word)
        # ascii str
        word = cls._tuple_ascii_str(tuple1=word)
        # reverse
        word = cls._reverse_tuple(tuple1=word)
        # extract senha
        senha = word[: passw.__len__()-2]
        senha += word[-2:]
        senha = cls._tuple_str(tuple1=senha)
        if senha != passw:
            return None
        else:
            senha = None
        # extract word
        word = word[passw.__len__()-2: -2]
        return cls._tuple_str(tuple1=word)

    # tools

    @classmethod
    def _change_int(cls, tuple1=()):
        secret, j = (), 1
        for i in range(tuple1.__len__()):
            if j > 5:
                j = 1
            secret += (tuple1[i] + j, )
            j += 1
        else:
            return secret

    @classmethod
    def _revert_int(cls, tuple1=()):
        secret, j = (), 1
        for i in range(tuple1.__len__()):
            if j > 5:
                j = 1
            secret += (tuple1[i] - j, )
            j += 1
        else:
            return secret

    @classmethod
    def _reverse_tuple(cls, tuple1=()):
        return tuple(tuple1[i] for i in
                     range(tuple1.__len__()-1, -1, -1))

    @classmethod
    def _tuple_ascii_str(cls, tuple1=()):
        return tuple(chr(_) for _ in tuple1)

    @classmethod
    def _tuple_ascii_int(cls, tuple1=()):
        return tuple(ord(_) for _ in tuple1)

    @classmethod
    def _str_tuple(cls, str1=''):
        return tuple(str1)

    @classmethod
    def _tuple_str(cls, tuple1=()):
        return ''.join(_ for _ in tuple1)

    @classmethod
    def _mix_strs(cls, str1='', str2=''):
        return str2[:-2] + str1 + str2[-2:]

    @classmethod
    def _add_equals(cls, tuple1=()):
        return tuple1 + ('=',) * 2

    @classmethod
    def _delete_equals(cls, str1=''):
        return str1[:-2]
