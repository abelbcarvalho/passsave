from random import choice
from com.passgen.model.passgen import PassGen
from com.passgen.maker.i_pass_maker import IPassMaker


class PassMaker(IPassMaker):
    """Essa classe é a responsável por gerar
    uma senha com base nos critérios fornecidos
    pelo usuário.

    Args:
        IPassMaker (interface): classe
        abstrata com os metodos necessários.
        Devem ser expandidos.

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """Gere uma Nova Senha Aleatória.
        """
        super().__init__()

    def generate_password(self, passgen: PassGen) -> str:
        """Metodo Gerador de Senhas.

        Args:
            passgen (PassGen): Instancia com os parametros
            necessários e aprovados no service.

        Returns:
            str: senha gerada.
        """
        password, data = '', ()
        chars = (
            self._gen_numbers(passgen.numbers),
            self._gen_upper(passgen.upcase),
            self._gen_lower(passgen.lowcase),
            self._gen_symbol_1(passgen.symbol_1),
            self._gen_symbol_2(passgen.symbol_2),
            self._gen_symbol_3(passgen.symbol_3),
        )
        chars = tuple(i for i in chars if i)
        for i in chars:
            data += tuple(_ for _ in i)
        else:
            chars, _ = None, None
        for i in range(passgen.size):
            password += choice(data)
        else:
            data, i = None, None
            return password

    def _gen_numbers(self, allow: bool):
        return (chr(i) for i in range(48, 58)) if allow else ''

    def _gen_upper(self, allow: bool):
        return (chr(i) for i in range(65, 91)) if allow else ''

    def _gen_lower(self, allow: bool):
        return (chr(i) for i in range(97, 123)) if allow else ''

    def _gen_symbol_1(self, allow: bool):
        return (chr(i) for i in range(33, 48)) if allow else ''

    def _gen_symbol_2(self, allow: bool):
        return (chr(i) for i in range(58, 65)) if allow else ''

    def _gen_symbol_3(self, allow: bool):
        return (chr(i) for i in range(91, 97)) if allow else ''
