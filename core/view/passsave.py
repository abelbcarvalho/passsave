from tkinter import Entry, Checkbutton
from tkinter import Tk, Frame, Label, Button, Menu
from tkinter.ttk import Treeview
from tkinter.constants import LEFT, RIGHT
from com.account.model.account import Account
from com.login.model.login import Login
from com.info.model.info import Info
from com.passgen.view.genpass import GenPass
from com.login.view.logincreate import LoginCreate
from com.info.view.infocreate import InfoCreate
from core.view.perfil import Perfil


class PassSave:
    """Tela principal da aplicação.

    Author:
        abelbcarvalho
    """

    _font_default = ('Courier 10 Pitch', 17)
    _font_pequena = (_font_default[0], 12)
    _colunas_log = tuple(f'coluna-{i}' for i in range(7))
    _colunas_info = tuple(f'coluna-{i}' for i in range(5))

    def __init__(self, account=Account()) -> None:
        """Construtor.

        Args:
            account (Account): carregar usuário do aplicativo.
        """
        self._account = account
        self._login = Login()
        self._info = Info()
        self._login.fk = self._account.id
        self._info.fk = self._login.fk
        # onde tudo começa
        self.window = Tk()
        self.window.title('Passsave - Gerencie Acesso')
        self.window.minsize(720, 512)

        self.menubar = Menu(self.window)
        self.filemenu = Menu(self.menubar)
        self.filemenu.add_command(label='Perfil', command=self._goto_perfil)
        self.filemenu.add_command(label='Excluir Conta')
        self.filemenu.add_command(label='Sair')
        self.menubar.add_cascade(label="Arquivo", menu=self.filemenu)

        self.editmenu = Menu(self.menubar)
        self.editmenu.add_command(label='Copiar')
        self.editmenu.add_command(label='Colar')
        self.menubar.add_cascade(label='Editar', menu=self.editmenu)

        self.toolmenu = Menu(self.menubar)
        self.toolmenu.add_command(
            label='Gerador de Senha', command=self._generate_pass)
        self.menubar.add_cascade(label='Ferramentas', menu=self.toolmenu)

        self.helpmenu = Menu(self.menubar)
        self.helpmenu.add_command(label='Tutorial')
        self.helpmenu.add_command(label='Sobre a BCarSoft')
        self.menubar.add_cascade(label='Ajuda', menu=self.helpmenu)

        self.window.config(menu=self.menubar)

        self.begin_frame = Frame(self.window)
        self.begin_frame.pack()

        self.title_label = Label(self.begin_frame)
        self.title_label['font'] = self._font_default
        self.title_label['text'] = 'PassSave - Salve suas informarções de Login'
        self.title_label.pack()

        self.pesq_log_frame = Frame(self.window)
        self.pesq_log_frame.pack()

        self.pesq_log_entry = Entry(self.pesq_log_frame)
        self.pesq_log_entry['font'] = self._font_pequena
        self.pesq_log_entry['width'] = 20
        self.pesq_log_entry.pack(side=LEFT)

        self.pesq_log_id_chk = Checkbutton(
            self.pesq_log_frame,
            text="Por ID",
        )
        self.pesq_log_id_chk['font'] = self._font_pequena
        self.pesq_log_id_chk.pack(side=LEFT)

        self.pesq_log_user_chk = Checkbutton(
            self.pesq_log_frame,
            text="Por Usuário",
        )
        self.pesq_log_user_chk['font'] = self._font_pequena
        self.pesq_log_user_chk.pack(side=LEFT)

        self.pesq_log_email_chk = Checkbutton(
            self.pesq_log_frame,
            text="Por E-Mail",
        )
        self.pesq_log_email_chk['font'] = self._font_pequena
        self.pesq_log_email_chk.pack(side=LEFT)

        self.pesq_log_data_chk = Checkbutton(
            self.pesq_log_frame,
            text="Por Data",
        )
        self.pesq_log_data_chk['font'] = self._font_pequena
        self.pesq_log_data_chk.pack(side=LEFT)

        self.pesq_log_mes_chk = Checkbutton(
            self.pesq_log_frame,
            text="Por Mês",
        )
        self.pesq_log_mes_chk['font'] = self._font_pequena
        self.pesq_log_mes_chk.pack(side=LEFT)

        self.pesq_log_ano_chk = Checkbutton(
            self.pesq_log_frame,
            text="Por Ano",
        )
        self.pesq_log_ano_chk['font'] = self._font_pequena
        self.pesq_log_ano_chk.pack(side=LEFT)

        self.login_frame = Frame(self.window)
        self.login_frame.pack()

        self.login_label = Label(self.login_frame)
        self.login_label['font'] = self._font_default
        self.login_label['text'] = 'Aqui estão os logins deste Usuário'
        self.login_label.pack()

        self.login_table = Treeview(
            self.login_frame, column=self._colunas_log, selectmod='browse', show='headings')
        self.login_table.column(
            self._colunas_log[0], width=70, minwidth=20, stretch='NO')
        self.login_table.heading('#1', text='ID')
        self.login_table.column(
            self._colunas_log[1], width=150, minwidth=70, stretch='NO')
        self.login_table.heading('#2', text='Nome')
        self.login_table.column(
            self._colunas_log[2], width=150, minwidth=70, stretch='NO')
        self.login_table.heading('#3', text='Link')
        self.login_table.column(
            self._colunas_log[3], width=150, minwidth=70, stretch='NO')
        self.login_table.heading('#4', text='Usuário')
        self.login_table.column(
            self._colunas_log[4], width=150, minwidth=70, stretch='NO')
        self.login_table.heading('#5', text='Email')
        self.login_table.column(
            self._colunas_log[5], width=150, minwidth=70, stretch='NO')
        self.login_table.heading('#6', text='Senha')
        self.login_table.column(
            self._colunas_log[6], width=150, minwidth=70, stretch='NO')
        self.login_table.heading('#7', text='Data')
        self.login_table.pack(padx=30)

        self.button_frame = Frame(self.window)
        self.button_frame.pack()

        self.butt_create_info = Button(self.button_frame)
        self.butt_create_info['width'] = 11
        self.butt_create_info['font'] = self._font_pequena
        self.butt_create_info['text'] = 'Novo Info'
        self.butt_create_info['fg'] = '#ffffff'
        self.butt_create_info['bg'] = '#002b36'
        self.butt_create_info.bind('<Button-1>', self._create_info)
        self.butt_create_info.pack(side=LEFT, pady=7, padx=7)

        self.butt_delete_info = Button(self.button_frame)
        self.butt_delete_info['width'] = 11
        self.butt_delete_info['font'] = self._font_pequena
        self.butt_delete_info['text'] = 'Delete Info'
        self.butt_delete_info['fg'] = '#ffffff'
        self.butt_delete_info['bg'] = '#d93a05'
        self.butt_delete_info.pack(side=LEFT, pady=7, padx=7)

        self.butt_delete_login = Button(self.button_frame)
        self.butt_delete_login['width'] = 11
        self.butt_delete_login['font'] = self._font_pequena
        self.butt_delete_login['text'] = 'Delete Login'
        self.butt_delete_login['fg'] = '#ffffff'
        self.butt_delete_login['bg'] = '#d93a05'
        self.butt_delete_login.pack(side=RIGHT, pady=7, padx=7)

        self.butt_create_login = Button(self.button_frame)
        self.butt_create_login['width'] = 11
        self.butt_create_login['font'] = self._font_pequena
        self.butt_create_login['text'] = 'Novo Login'
        self.butt_create_login['fg'] = '#ffffff'
        self.butt_create_login['bg'] = '#002b36'
        self.butt_create_login.bind('<Button-1>', self._create_login)
        self.butt_create_login.pack(side=RIGHT, pady=7, padx=7)

        self.info_frame = Frame(self.window)
        self.info_frame.pack()

        self.info_label = Label(self.info_frame)
        self.info_label['font'] = self._font_default
        self.info_label['text'] = 'Aqui estão as informações adicionais deste Login'
        self.info_label.pack()

        self.info_table = Treeview(
            self.info_frame, column=self._colunas_info, selectmod='browse', show='headings')
        self.info_table.column(
            self._colunas_info[0], width=70, minwidth=20, stretch='NO')
        self.info_table.heading('#1', text='ID')
        self.info_table.column(
            self._colunas_info[1], width=220, minwidth=200, stretch='NO')
        self.info_table.heading('#2', text='Token')
        self.info_table.column(
            self._colunas_info[2], width=220, minwidth=200, stretch='NO')
        self.info_table.heading('#3', text='Comentário')
        self.info_table.column(
            self._colunas_info[3], width=150, minwidth=70, stretch='NO')
        self.info_table.heading('#4', text='Data')
        self.info_table.column(
            self._colunas_info[4], width=70, minwidth=20, stretch='NO')
        self.info_table.heading('#5', text='IDL')
        self.info_table.pack(padx=30, pady=10)

        self.window.mainloop()

    def _generate_pass(self) -> None:
        """Chama tela de gerador de senha.
        """
        GenPass()
    
    def _goto_perfil(self) -> None:
        """Vai para tela de possíveis edições
        na conta do aplicativo.
        """
        Perfil(account=self._account)
    
    def _create_login(self, evt) -> None:
        """Chama tela de criar Login.

        Args:
            evt (mouse): <Button-1>
        """
        LoginCreate(login=self._login)
    
    def _create_info(self, evt) -> None:
        """Chama a tela de criar Info.

        Args:
            evt (mouse): <Button-1>
        """
        InfoCreate(info=self._info)

