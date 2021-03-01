from com.info.model.info import Info
from com.info.service.i_service_info import IServiceInfo
from tools.general import is_none_empty
from tools.general import is_great_than
from tools.name_check import NameCheck
from tools.data_check import DataCheck
from com.info.dao.dao_info import DAOInfo
from core.singleton.sing_message import SingMessage as Msg
from encript.encript import Encript


class ServiceInfo(IServiceInfo):
    """Regra de negócio para Info.

    Args:
        IServiceInfo (interface): classe
        abstrata que simula interface e
        possuí os metódos para essa classe.

    Author:
        abelbcarvalho
    """

    def __init__(self) -> None:
        """Novo Service de Info.
        """
        super().__init__()
        self._dao = DAOInfo()
        self._passw = 'uSRj5ZFduUSk1jTDmOWN0FTKUoRwTK'

    # metodos crud

    def create_info(self, info: Info) -> bool:
        """Esse metodo tentará Criar Info.

        Args:
            info (info): instância com dados
            necessários.

        Returns:
            bool: True se for criado.
        """
        if not isinstance(info, Info):
            Msg.message().setmessage(key='intance')
            return False
        elif not self._checker_create_update(info=info):
            return False
        else:
            sql = 'insert into tbInfo ('
            sql += 'comment,inform,dia,mes,ano,id_log) '
            sql += 'values (?' + 5 * ',?' + ')'
            if self._dao.create_info(info=info, sql=sql):
                Msg.message().setmessage(key='info-c', sucesso=True)
                return True
            else:
                Msg.message().setmessage(key='info-c')
                return False

    def read_info(self, **kwargs) -> list:
        """Esse metodo servirá para realizar
        busca de Infos.

        Returns:
            list: lista de Infos ou None.
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
            if not not encripted:
                for i in encripted.keys():
                    kwargs[i] = encripted[i]
            data = self._dao.read_info(**kwargs)
            if not data:
                Msg.message().setmessage(key='info-s')
                return None
            else:
                infos = []
                Msg.message().setmessage(key='info-s', sucesso=True)
                for inf in data:
                    info = Info()
                    info.id = inf[0]
                    info.comment = Encript.decript(
                        word=inf[1], passw=self._passw)
                    info.inform = Encript.decript(
                        word=inf[2], passw=self._passw)
                    info.data.dia = inf[3]
                    info.data.mes = inf[4]
                    info.data.ano = inf[5]
                    info.fk = inf[6]
                    infos.append(info)
                return infos

    def update_info(self, info: Info) -> bool:
        """Esse metodo tentará Atualizar Info.

        Args:
            info (info): instância com dados
            necessários.

        Returns:
            bool: True se for atualizado.
        """
        if not isinstance(info, Info):
            Msg.message().setmessage(key='instancia')
            return False
        elif not info.id > 0:
            Msg.message().setmessage(key='chave')
            return False
        elif not self._checker_create_update(info=info):
            return False
        else:
            sql = 'update tbInfo set '
            sql += 'coment=?,inform=?,dia=?,mes=?,ano=?,id_log=? '
            sql += 'where id=?'
            if self._dao.update_info(info=info, sql=sql):
                Msg.message().setmessage(key='info-u', sucesso=True)
                return True
            else:
                Msg.message().setmessage(key='info-u')
                return False

    def delete_info(self, info: Info) -> bool:
        """Esse metodo tentará Deletar Info.

        Args:
            info (info): instância com dados
            necessários.

        Returns:
            bool: True se for deletado.
        """
        if not isinstance(info, Info):
            Msg.message().setmessage(key='instancia')
            return False
        elif not info.id > 0:
            Msg.message().setmessage(key='chave')
            return False
        else:
            sql = 'delete from tbInfo where id=?'
            if self._dao.delete_info(info=info, sql=sql):
                Msg.message().setmessage(key='info-d', sucesso=True)
                return True
            else:
                Msg.message().setmessage(key='info-d')
                return False

    def delete_all_info(self, sql='', fk=0) -> bool:
        """Esse metodo tenta deletar todas as infos
        de logins de uma pessoa no aplicativo.

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
            sql = 'delete from tbInfo where id_log=?'
            return self._dao.delete_all_info(sql=sql, fk=fk)

    # economizado linhas

    def _checker_create_update(self, info: Info) -> bool:
        """Esse metodo realiza a checagem para criar
        e atualizar, assim economiza linhas de código.

        Args:
            info (Info): Objeto com os dados.

        Returns:
            bool: True se a checagem foi okay.
        """
        if not info.fk > 0:
            Msg.message().setmessage(key='chave')
            return False
        elif is_none_empty(word=info.comment):
            Msg.message().setmessage(key='str')
            return False
        elif is_none_empty(word=info.inform):
            Msg.message().setmessage(key='str')
            return False
        elif NameCheck.is_name_okay(word=info.comment):
            Msg.message().mesg = 'Erro: Comentario Inválido.'
            return False
        elif is_great_than(word=info.comment, size=60):
            Msg.message().setmessage(key='str-size')
            return False
        elif is_great_than(word=info.inform, size=216):
            Msg.message().setmessage(key='str-size')
            return False
        elif not DataCheck.is_valid_data(data=info.data):
            Msg.message().setmessage(key='data')
            return False
        else:
            info.comment = Encript.encript(
                word=info.comment, passw=self._passw)
            info.inform = Encript.encript(word=info.inform, passw=self._passw)
            return True
