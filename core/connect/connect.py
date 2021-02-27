from sqlite3 import connect


class Connect:
    """Classe base para a criação
    de tabelas e os métodos de
    operação referente ao banco
    de dados sqlite3.

    Author:
        abelbcarvalho
    """

    _conexao = None
    _cursor = None

    @classmethod
    def create_tables(cls) -> None:
        """Criando as Tabelas pelos modelos.
        """
        model = 'create table if not exists {} ('
        table = model + '{},' * 10
        table = table[: -1] + ');'
        table = table.format(
            'tbAccount',
            'id integer not null primary key autoincrement',
            'nome varchar(80) not null',
            'sexo varchar(80) not null',
            'dia integer not null',
            'mes integer not null',
            'ano integer not null',
            'user varchar(80) not null',
            'email varchar(80) not null',
            'passw varchar(80) not null',
            'mobile varchar(80) not null',
        )
        tables = (table, )
        table = model + '{},' * 11
        table = table[: -1] + ');'
        table = table.format(
            'tbLogin',
            'id integer not null primary key autoincrement',
            'nome varchar(80) not null',
            'link varchar(100) not null',
            'user varchar(80) not null',
            'email varchar(80) not null',
            'passw varchar(80) not null',
            'dia integer not null',
            'mes integer not null',
            'ano integer not null',
            'id_acc int not null',
            'foreign key (id_acc) references tbAccount(id)',
        )
        tables += (table, )
        table = model + '{},' * 8
        table = table[: -1] + ');'
        table = table.format(
            'tbInfo',
            'id integer not null primary key autoincrement',
            'comment varchar(100) not null',
            'inform varchar(256) not null',
            'dia integer not null',
            'mes integer not null',
            'ano integer not null',
            'id_log int not null',
            'foreign key (id_log) references tbLogin(id)',
        )
        tables += (table, )
        try:
            cls.open_connection()
            for table in tables:
                cls.cursor().execute(table)
            cls.conexao().commit()
        except Exception as ex:
            print(ex)
            return None
        finally:
            cls.close_connection()
            tables = ()
            table = ''
            model = ''

    @classmethod
    def open_connection(cls):
        """Esse metódo abre uma conexão
        com banco de dados
        se não estiver aberta.
        """
        if not cls.conexao():
            cls._conexao = connect('database/passave.db')
            cls._cursor = cls.conexao().cursor()

    @classmethod
    def close_connection(cls):
        """Esse metódo fecha conexão
        se não estiver fechada.
        """
        if cls.conexao():
            cls._conexao = None
            cls._cursor = None

    # getter

    @classmethod
    def conexao(cls):
        """Retorna a conexão.
        """
        return cls._conexao

    @classmethod
    def cursor(cls):
        """Retorna o cursor.
        """
        return cls._cursor
