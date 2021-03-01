class Message:
    """Classe que poderá ser acessada
    com um singleton. Ela deve ser usada
    como uma forma de receber mensagens,
    quer sejam de erros ou sucesso.

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """Nova Mensagem.
        """
        self._mesg = ''

    def setmessage(self, key='', sucesso=False) -> None:
        """Esse metodo insere uma mensagem, seja ela
        de erro ou sucesso. Será possivel acessar pelo
        singleton.

        Args:
            key (str, optional): chave para mensagem. Defaults to ''.
            suceso (bool, optional): determina sucesso ou erro.
            Defaults to False.
        """
        self.mesg = self._gen_msg_error(key=key) if not sucesso \
            else self._gen_msg_success(key=key)

    def _gen_msg_error(self, key='') -> str:
        """Eess metodo poderá gerar uma mensagem de erro.

        Args:
            key (str, optional): chave. Defaults to ''.

        Returns:
            str: mensagem de erro se a chave existir.
        """
        error = {
            'account-c': 'Erro: Conta Não Criada.',
            'login-c': 'Erro: Login Não Criado.',
            'info-c': 'Erro: Info Não Criado.',
            'account-u': 'Erro: Conta Não Atualizada.',
            'login-u': 'Erro: Login Não Atualizado.',
            'info-u': 'Erro: Info Não Atualizado.',
            'account-s': 'Erro: Conta Não Encontrada.',
            'login-s': 'Erro: Login Não Encontrado.',
            'info-s': 'Erro: Info Não Encontrado.',
            'account-d': 'Erro: Conta Não Deletada.',
            'login-d': 'Erro: Login Não Deletada.',
            'info-d': 'Erro: Info Não Deletada.',
            'str': 'Erro: String Inválida.',
            'str-size': 'Erro: String Tamanho Inválido.',
            'data': 'Erro: Data Inválida.',
            'instancia': 'Erro: Instancia Inválida',
            'passw': 'Erro: Senha Inválida.',
            'chave': 'Erro: Chave de Acesso Inválida.'
        }
        return error[key] if key in error.keys() else ''

    def _gen_msg_success(self, key='') -> str:
        """Eess metodo poderá gerar uma mensagem de sucesso.

        Args:
            key (str, optional): chave. Defaults to ''.

        Returns:
            str: mensagem de sucesso se a chave existir.
        """
        sucesso = {
            'account-c': 'Sucesso: Conta Criada.',
            'login-c': 'Sucess: Login Criado.',
            'info-c': 'Sucesso: Info Criado.',
            'account-u': 'Sucesso: Conta Atualizada.',
            'login-u': 'Sucesso: Login Atualizado.',
            'info-u': 'Sucesso: Info Atualizado.',
            'account-s': 'Sucesso: Conta Encontrada.',
            'login-s': 'Sucesso: Login Encontrado.',
            'info-s': 'Sucesso: Info Encontrado.',
            'account-d': 'Sucesso: Conta Deletada.',
            'login-d': 'Sucesso: Login Deletado.',
            'info-d': 'Sucessi: Info Deletado.',
        }
        return sucesso[key] if key in sucesso.keys() else ''

    @property
    def mesg(self) -> str:
        return self._mesg

    @mesg.setter
    def mesg(self, mesg: str) -> None:
        self._mesg = mesg
