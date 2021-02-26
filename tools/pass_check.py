from tools.general import is_none_empty
from tools.general import is_great_than
from tools.general import make_str_list_each


class PassCheck:
    """
    Essa classe funciona como um verificador
    para validação de senhas de usuário para
    aplicação.
    [Somente com Metodos de Classe.]

    Author:
        abelbcarvalho
    """

    # senhas gerais

    @classmethod
    def verifica_senha_app(cls, senha='', size=16) -> bool:
        """Verifica se a senha pode ser considerada
        válida.

        Args:
            senha (str, optional): senha. Defaults to ''.
            size (int, optional): tamanho. Defaults to 16.

        Returns:
            bool: True se a senha for válida.
        """
        if is_none_empty(senha):
            return False
        elif is_great_than(senha, size):
            return False
        return cls._valid_characters(senha)

    @classmethod
    def _valid_characters(cls, senha='') -> bool:
        """Esse metodo verifica se os caracteres são válidos
        através da tabela ascii. [#,$,%,&,0...9,@,A...Z,a...z]

        Args:
            senha (str, optional): senha a ser verificada.
            Defaults to ''.

        Returns:
            bool: True se caraceteres válidos.
        """
        aux = make_str_list_each(senha)
        aux = [ord(c) for c in aux]
        for c in aux:
            if c < 35 or c > 122:
                return False
            if 38 < c < 48:
                return False
            if 57 < c < 64:
                return False
            if 90 < c < 97:
                return False
        else:
            return True
