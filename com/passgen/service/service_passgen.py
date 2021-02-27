from com.passgen.model.passgen import PassGen
from com.passgen.service.i_service_passgen import IServicePassGen
from com.passgen.maker.pass_maker import PassMaker


class ServicePassGen(IServicePassGen):
    """Regra de Negócio para geração de senhas.

    Args:
        IServicePassGen (interface): possuí metodo que
        retornará senha.
    """

    def __init__(self) -> None:
        """Gerar Nova Senha.
        """
        super().__init__()
        self._pass = PassMaker()

    def generate_password(self, passgen: PassGen) -> str:
        """Gerar Nova Senha.

        Args:
            passgen (PassGen): Dados para que seja gerada
            a senha.

        Returns:
            str: senha gerada ou None.
        """
        if not isinstance(passgen, PassGen):
            return ''
        invalid = 0
        if not passgen.numbers:
            invalid += 1
        if not passgen.upcase:
            invalid += 1
        if not passgen.lowcase:
            invalid += 1
        if not passgen.symbol_1:
            invalid += 1
        if not passgen.symbol_2:
            invalid += 1
        if not passgen.symbol_3:
            invalid += 1
        if not passgen.size > 0:
            invalid += 1
        return '' if invalid == 7 else \
            self._pass.generate_password(passgen=passgen)
