from tkinter import Tk, Frame, Label, Button, Menu
from tkinter.ttk import Treeview


class PassSave:
    """Tela principal da aplicação.

    Author:
        abelbcarvalho
    """

    _font_default = ('Courier 10 Pitch', 17)
    _font_pequena = (_font_default[0], 12)
    _colunas_log = tuple(f'coluna-{i}' for i in range(7))
    _colunas_info = tuple(f'coluna-{i}' for i in range(5))

    def __init__(self) -> None:
        """Construtor.
        """
        self.window = Tk()
        self.window.title('Passsave - Gerencie Acesso')
        self.window.minsize(720, 512)

        self.menubar = Menu(self.window)
        self.filemenu = Menu(self.menubar)
        self.filemenu.add_command(label='Abrir')
        self.filemenu.add_command(label='Perfil')
        self.filemenu.add_command(label='Salvar')
        self.filemenu.add_command(label='Sair')
        self.menubar.add_cascade(label="Arquivo", menu=self.filemenu)

        self.editmenu = Menu(self.menubar)
        self.editmenu.add_command(label='Copiar')
        self.editmenu.add_command(label='Colar')
        self.menubar.add_cascade(label='Editar', menu=self.editmenu)

        self.toolmenu = Menu(self.menubar)
        self.toolmenu.add_command(label='Gerador de Senha')
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
        self.login_table.pack(padx=30, pady=10)

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
            self._colunas_info[1], width=150, minwidth=70, stretch='NO')
        self.info_table.heading('#2', text='Token')
        self.info_table.column(
            self._colunas_info[2], width=150, minwidth=70, stretch='NO')
        self.info_table.heading('#3', text='Comentário')
        self.info_table.column(
            self._colunas_info[3], width=150, minwidth=70, stretch='NO')
        self.info_table.heading('#4', text='Data')
        self.info_table.column(
            self._colunas_info[4], width=70, minwidth=20, stretch='NO')
        self.info_table.heading('#5', text='IDL')
        self.info_table.pack(padx=30, pady=10)

        self.window.mainloop()


if __name__ == '__main__':
    PassSave()
