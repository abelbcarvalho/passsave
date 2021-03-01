from com.login.service.i_service_login \
    import IServiceLogin
from tools.data_check import DataCheck
from tools.pass_check import PassCheck
from tools.email_check import EmailCheck
from tools.user_check import UserCheck
from tools.general import is_great_than
from tools.general import is_none_empty
from tools.name_check import NameCheck
from com.login.model.login import Login
from com.login.dao.dao_login import DAOLogin
from core.singleton.sing_message import SingMessage as Msg
from encript.encript import Encript


class ServiceLogin(IServiceLogin):
    """Regra de negócio para Login.

    Args:
        IServiceLogin (interface): classe
        abstrata que simula interface e
        possuí os metódos para essa classe.

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """Novo Service de Login.
        """
        super().__init__()
        self._dao = DAOLogin()
        self._passw = 'g2ycveUijWE1cnRccO5QlRugjsDtY6'

    # metodos crud

    def create_login(self, login: Login) -> bool:
        """Esse metodo tentará Criar Login.

        Args:
            login (Login): instância com dados
            necessários.

        Returns:
            bool: True se for criado.
        """
        if not isinstance(login, Login):
            Msg.message().setmessage(key='instancia')
            return False
        elif not self._checker_create_update(login=login):
            return False
        else:
            sql = 'insert into tbLogin ('
            sql += 'nome,link,user,email,passw,dia,mes,ano,id_acc) '
            sql += 'values (?' + 8 * ',?' + ')'
            if self._dao.create_login(login=login, sql=sql):
                Msg.message().setmessage(key='login-c', sucesso=True)
                return True
            else:
                Msg.message().setmessage(key='login-c')
                return False

    def read_login(self, **kwargs) -> list:
        """Esse metodo servirá para realizar
        busca de logins.

        Returns:
            list: lista de Logins ou None.
        """
        if not kwargs:
            Msg.message().mesg = 'Erro: Dados Inválidos.'
            return None
        elif not 'sql' in kwargs.keys():
            Msg.message().mesg = 'Erro: Query SQL Não Encontrada.'
            return None
        else:
            encripted = {
                i: Encript.encript(word=kwargs[i], passw=self._passw)
                for i in kwargs.keys() if isinstance(kwargs[i], str)
            }
            for i in encripted.keys():
                kwargs[i] = encripted[i]
            else:
                encripted = None
            data = self._dao.read_login(**kwargs)
            if not data:
                Msg.message().setmessage(key='login-s')
                return None
            else:
                logins = []
                Msg.message().setmessage(key='login-s', sucesso=True)
                for log in data:
                    logi = Login()
                    logi.id = log[0]
                    logi.nome = Encript.decript(word=log[1], passw=self._passw)
                    logi.link = Encript.decript(word=log[2], passw=self._passw)
                    logi.user = Encript.decript(word=log[3], passw=self._passw)
                    logi.email = Encript.decript(
                        word=log[4], passw=self._passw)
                    logi.passw = Encript.decript(
                        word=log[5], passw=self._passw)
                    logi.data.dia = log[6]
                    logi.data.mes = log[7]
                    logi.data.ano = log[8]
                    logi.fk = log[9]
                    logins.append(logi)
                return logins

    def update_login(self, login: Login) -> bool:
        """Esse metodo tentará Atualizar Login.

        Args:
            login (Login): instância com dados
            necessários.

        Returns:
            bool: True se for atualizado.
        """
        if not isinstance(login, Login):
            Msg.message().setmessage(key='instancia')
            return False
        elif not login.id > 0:
            Msg.message().setmessage(key='chave')
            return False
        elif not self._checker_create_update(login=login):
            return False
        else:
            sql = 'update tbLogin set nome=?,link=?,user=?,email=?,'
            sql += 'passw=?,dia=?,mes=?,ano=?,id_acc=? where id=?'
            if self._dao.update_login(login=login, sql=sql):
                Msg.message().setmessage(key='login-u', sucesso=True)
                return True
            else:
                Msg.message().setmessage(key='login-u')
                return False

    def delete_login(self, login: Login) -> bool:
        """Esse metodo tentará Deletar Login.

        Args:
            login (Login): instância com dados
            necessários.

        Returns:
            bool: True se for deletado.
        """
        if not isinstance(login, Login):
            Msg.message().setmessage(key='instancia')
            return False
        elif not login.id > 0:
            Msg.message().setmessage(key='chave')
            return False
        else:
            sql = 'delete from tbLogin where id=?'
            if self._dao.delete_login(login=login, sql=sql):
                Msg.message().setmessage(key='login-d', sucesso=True)
                return True
            else:
                Msg.message().setmessage(key='login-d')
                return False

    def delete_all_login(self, sql='', fk=0) -> bool:
        """Esse metodo tenta deletar todas as contas
        de usuário de uma pessoa no aplicativo.

        Args:
            sql (str, optional): sql query. Defaults to ''.
            fk (int, optional): chave estrangeira. Defaults to 0.

        Returns:
            bool: True se deletado.
        """
        if not sql:
            return False
        elif not isinstance(sql, str):
            return False
        elif not isinstance(fk, int):
            return False
        else:
            sql = 'delete from tbLogin where id_acc=?'
            return self._dao.delete_all_login(sql=sql, fk=fk)

    def _checker_create_update(self, login: Login) -> bool:
        """Realiza checkagem de create e update.

        Args:
            login (Login): Objeto com os dados.

        Returns:
            bool: True se tudo okay.
        """
        if is_none_empty(word=login.nome):
            Msg.message().setmessage(key='str-size')
            return False
        elif not NameCheck.is_name_okay(word=login.nome):
            Msg.message().mesg = 'Erro: Nome de Site.'
            return False
        elif is_great_than(word=login.nome, size=40):
            Msg.message().setmessage(key='str-size')
            return False
        elif is_none_empty(word=login.link):
            Msg.message().mesg = 'Erro: Link Vázio.'
            return False
        elif is_great_than(word=login.link, size=50):
            Msg.message().setmessage(key='str-size')
            return False
        elif not UserCheck.validar_nome_usuario(usuario=login.user):
            Msg.message().mesg = 'Erro: Nome de Usuário.'
            return False
        elif not EmailCheck.email_is_valid(email=login.email):
            Msg.message().mesg = 'Erro: Email Inválido.'
            return False
        elif not PassCheck.verifica_senha_app(senha=login.passw, size=40):
            Msg.message().setmessage(key='passw')
            return False
        elif not DataCheck.is_valid_data(data=login.data):
            Msg.message().setmessage(key='data')
            return False
        elif not login.fk > 0:
            Msg.message().setmessage(key='chave')
            return False
        else:
            login.nome = Encript.encript(word=login.nome, passw=self._passw)
            login.link = Encript.encript(word=login.link, passw=self._passw)
            login.user = Encript.encript(word=login.user, passw=self._passw)
            login.email = Encript.encript(word=login.email, passw=self._passw)
            login.passw = Encript.encript(word=login.passw, passw=self._passw)
            return True
