from com.account.service.i_service_account import IServiceAccount
from tools.general import is_absolute_equal, is_great_than
from tools.general import tira_espacos_inicio_final
from tools.general import is_none_empty
from tools.name_check import NameCheck
from tools.data_check import DataCheck
from tools.user_check import UserCheck
from tools.email_check import EmailCheck
from tools.pass_check import PassCheck
from tools.mobile_check import MobileCheck
from com.account.model.account import Account
from com.account.dao.dao_account import DAOAccount
from core.singleton.sing_message import SingMessage as Msg


class ServiceAccount(IServiceAccount):
    """Regra de negócio para Account.

    Args:
        IServiceAccount (interface): classe
        abstrata que simula interface e
        possuí os metódos para essa classe.

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """Novo Service de Account.
        """
        super().__init__()
        self._dao = DAOAccount()

    # metodos crud

    def create_account(self, account: Account) -> bool:
        """Esse metodo tentará Criar Account.

        Args:
            account (Account): instância com dados
            necessários.

        Returns:
            bool: True se for criado.
        """
        if not isinstance(account, Account):
            Msg.message().setmessage(key='instancia')
            return False
        account.nome = tira_espacos_inicio_final(word=account.nome) \
            if account.nome else ''
        account.sexo = tira_espacos_inicio_final(word=account.sexo) \
            if account.sexo else ''
        if not self._cheker_for_create_update(account=account):
            return False
        else:
            sql = 'insert into tbAccount ('
            sql += 'nome,sexo,dia,mes,ano,user,email,passw,mobile'
            sql += ') values (?' + ',?' * 8 + ')'
            if self._dao.create_account(account=account, sql=sql):
                Msg.message().setmessage(key='account-c', sucesso=True)
                return True
            else:
                Msg.message().setmessage(key='account-c')
                return False

    def read_account(self, **kwargs) -> list:
        """Esse metodo tentará entrar no aplicativo
        com um dicionário como parametro - **kwargs
        deve existir:
        - user, email, passw

        Returns:
            list: Account list se encontrado else None.
        """
        if not kwargs:
            Msg.message().mesg = 'Erro: Dados Inválidos.'
            return None
        elif not 'user' in kwargs.keys():
            Msg.message().mesg = 'Erro: Usuário Inválido.'
            return None
        elif not 'email' in kwargs.keys():
            Msg.message().mesg = 'Erro: Usuário Inválido.'
            return None
        elif not 'passw' in kwargs.keys():
            Msg.message().setmessage(key='passw')
            return None
        sql = 'select * from tbAccount where (user=? '
        sql += 'or email=?) and passw=?'
        kwargs['sql'] = sql
        data = self._dao.read_account(**kwargs)
        if not data:
            Msg.message().setmessage(key='account-s')
            return None
        else:
            accounts = []
            Msg.message().setmessage(key='account-s', sucesso=True)
            for acc in data:
                account = Account()
                account.id = acc[0]
                account.nome = acc[1]
                account.sexo = acc[2]
                account.nasc.dia = acc[3]
                account.nasc.mes = acc[4]
                account.nasc.ano = acc[5]
                account.user = acc[6]
                account.email = acc[7]
                account.passw = acc[8]
                account.mobile = acc[9]
                accounts.append(account)
            return accounts

    def update_account(self, account: Account) -> bool:
        """Esse metodo tentará Atualizar Ac)count.

        Args:
            account (Account): instância com dados
            necessários.

        Returns:
            bool: True se for atualizado.
        """
        if not isinstance(account, Account):
            Msg.message().setmessage(key='instancia')
            return False
        account.nome = tira_espacos_inicio_final(word=account.nome) \
            if account.nome else ''
        account.sexo = tira_espacos_inicio_final(word=account.sexo) \
            if account.sexo else ''
        if not account.id > 0:
            Msg.message().setmessage(key='chave')
            return False
        elif not self._cheker_for_create_update(account=account):
            return False
        else:
            sql = 'update tbAccount set nome=?, sexo=?, dia=?, '
            sql += 'mes=?, ano=?, user=?, '
            sql += 'email=?, passw=?, mobile=? where id=?'
            if self._dao.update_account(account=account, sql=sql):
                Msg.message().setmessage(key='account-u', sucesso=True)
                return True
            else:
                Msg.message().setmessage(key='account-u')
                return False

    def delete_account(self, account: Account) -> bool:
        """Esse metodo tentará Deletar Account.

        Args:
            account (Account): instância com dados
            necessários.

        Returns:
            bool: True se for deletado.
        """
        if not isinstance(account, Account):
            Msg.message().setmessage(key='instancia')
            return False
        elif not account.id > 0:
            Msg.message().setmessage(key='chave')
            return False
        else:
            sql = 'delete from tbAccount where id=?'
            if self._dao.delete_account(account=account, sql=sql):
                Msg.message().setmessage(key='account-d', sucesso=True)
                return True
            else:
                Msg.message().setmessage(key='account-d')
                return False

    def _cheker_for_create_update(self, account: Account) -> bool:
        """Esse metodo serve para economizar linhas de codigo
        entre create e update.

        Args:
            account (Account): Account instance.

        Returns:
            bool: True se dados okay.
        """
        if is_none_empty(word=account.nome):
            Msg.message().setmessage(key='str-size')
            return False
        elif is_none_empty(word=account.sexo):
            Msg.message().setmessage(key='str-size')
            return False
        elif is_great_than(word=account.nome, size=45):
            Msg.message().setmessage(key='str-size')
            return False
        elif is_great_than(word=account.sexo, size=9):
            Msg.message().setmessage(key='str-size')
            return False
        elif not NameCheck.is_name_okay(word=account.nome):
            Msg.message().mesg = 'Erro: Nome Inválido.'
            return False
        elif not NameCheck.is_name_okay(word=account.sexo):
            Msg.message().setmessage(key='str')
            return False
        elif not is_absolute_equal(word=account.sexo, compare='feminino') \
            and not is_absolute_equal(word=account.sexo, compare='masculino') \
                and not is_absolute_equal(word=account.sexo, compare='hidden'):
            Msg.message().mesg = 'Erro: Sexo Inválido.'
            return False
        elif not DataCheck.is_valid_data(data=account.nasc):
            Msg.message().setmessage(key='data')
            return False
        elif not UserCheck.validar_nome_usuario(usuario=account.user):
            Msg.message().mesg = 'Erro: Nome de Usuário.'
            return False
        elif not EmailCheck.email_is_valid(email=account.email):
            Msg.message().mesg = 'Erro: Email Inválido.'
            return False
        elif not PassCheck.verifica_senha_app(senha=account.passw):
            Msg.message().setmessage(key='passw')
            return False
        elif not MobileCheck.mobile_valid(mobile=account.mobile):
            Msg.message().mesg = 'Erro: Celular Inválido.'
            return False
        else:
            return True
