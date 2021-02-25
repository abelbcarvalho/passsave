class Encript:
    """
    Class that can generate encripted strings as well
    it can return the original too.
    abelbcarvalho
    """

    def __init__(self):
        """
        New instance of Encript class.
        """
        pass

    def encript(self, word='', passw=''):
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
        word = self._mix_strs(str1=word, str2=passw)
        passw = None
        # become tuple
        word = self._str_tuple(str1=word)
        # reverse
        word = self._reverse_tuple(tuple1=word)
        # to ascii int
        word = self._tuple_ascii_int(tuple1=word)
        # change values
        word = self._change_int(tuple1=word)
        # to ascii str
        word = self._tuple_ascii_str(tuple1=word)
        # add equals
        word = self._add_equals(tuple1=word)
        # tuple in str
        return self._tuple_str(tuple1=word)

    def decript(self, word='', passw=''):
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
        word = self._delete_equals(str1=word)
        # str in tuple
        word = self._str_tuple(str1=word)
        # ascii int
        word = self._tuple_ascii_int(tuple1=word)
        # revert int
        word = self._revert_int(tuple1=word)
        # ascii str
        word = self._tuple_ascii_str(tuple1=word)
        # reverse
        word = self._reverse_tuple(tuple1=word)
        # extract senha
        senha = word[: passw.__len__()-2]
        senha += word[-2:]
        senha = self._tuple_str(tuple1=senha)
        if senha != passw:
            return None
        else:
            senha = None
        # extract word
        word = word[passw.__len__()-2: -2]
        return self._tuple_str(tuple1=word)

    # tools

    def _change_int(self, tuple1=()):
        secret, j = (), 1
        for i in range(tuple1.__len__()):
            if j > 5:
                j = 1
            secret += (tuple1[i] + j, )
            j += 1
        else:
            return secret

    def _revert_int(self, tuple1=()):
        secret, j = (), 1
        for i in range(tuple1.__len__()):
            if j > 5:
                j = 1
            secret += (tuple1[i] - j, )
            j += 1
        else:
            return secret

    def _reverse_tuple(self, tuple1=()):
        return tuple(tuple1[i] for i in
                     range(tuple1.__len__()-1, -1, -1))

    def _tuple_ascii_str(self, tuple1=()):
        return tuple(chr(_) for _ in tuple1)

    def _tuple_ascii_int(self, tuple1=()):
        return tuple(ord(_) for _ in tuple1)

    def _str_tuple(self, str1=''):
        return tuple(str1)

    def _tuple_str(self, tuple1=()):
        return ''.join(_ for _ in tuple1)

    def _mix_strs(self, str1='', str2=''):
        return str2[:-2] + str1 + str2[-2:]

    def _add_equals(self, tuple1=()):
        return tuple1 + ('=',) * 2

    def _delete_equals(self, str1=''):
        return str1[:-2]
