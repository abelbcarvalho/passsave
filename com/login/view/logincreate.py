from tkinter import messagebox
from tkinter import Tk, Frame, Label, Entry, Button
from tkinter.constants import LEFT
from com.login.model.login import Login
from core.singleton.sing_facade import SingFacade as Fac
from core.singleton.sing_message import SingMessage as Msg


class LoginCreate:
    """Classe de tela para criação de Login.

    Author:
        abelbcarvalho
    """

    _font_default = ('Courier 10 Pitch', 17)
    _font_pequena = (_font_default[0], 12)

    def __init__(self, login=Login()):
        """Nova Tela de Criação de Login.
        """
        self._login = login
        self.window = Tk()
        self.window.minsize(512, 420)
        self.window.maxsize(512, 420)
        self.window.title('PassSave - Registar Login')

        self.main_frame = Frame(self.window)
        self.main_frame.pack()

        self.title_label = Label(self.main_frame)
        self.title_label['font'] = self._font_default
        self.title_label['text'] = 'Registre Novo Login'
        self.title_label.pack(pady=15)

        self.site_label = Label(self.main_frame)
        self.site_label['font'] = self._font_pequena
        self.site_label['text'] = 'Nome do Site*'
        self.site_label.pack()

        self.site_entry = Entry(self.main_frame)
        self.site_entry['width'] = 40
        self.site_entry['font'] = self._font_pequena
        self.site_entry.pack()

        self.link_label = Label(self.main_frame)
        self.link_label['font'] = self._font_pequena
        self.link_label['text'] = 'Link do Site*'
        self.link_label.pack()

        self.link_entry = Entry(self.main_frame)
        self.link_entry['width'] = 40
        self.link_entry['font'] = self._font_pequena
        self.link_entry.pack()

        self.user_label = Label(self.main_frame)
        self.user_label['font'] = self._font_pequena
        self.user_label['text'] = 'Nome de Usuário*'
        self.user_label.pack()

        self.user_entry = Entry(self.main_frame)
        self.user_entry['width'] = 40
        self.user_entry['font'] = self._font_pequena
        self.user_entry.pack()

        self.email_label = Label(self.main_frame)
        self.email_label['font'] = self._font_pequena
        self.email_label['text'] = 'Endereço de E-Mail*'
        self.email_label.pack()

        self.email_entry = Entry(self.main_frame)
        self.email_entry['width'] = 40
        self.email_entry['font'] = self._font_pequena
        self.email_entry.pack()

        self.senha_label = Label(self.main_frame)
        self.senha_label['font'] = self._font_pequena
        self.senha_label['text'] = 'Senha*'
        self.senha_label.pack()

        self.senha_entry = Entry(self.main_frame)
        self.senha_entry['width'] = 40
        self.senha_entry['font'] = self._font_pequena
        self.senha_entry.pack()

        self.data_label = Label(self.main_frame)
        self.data_label['font'] = self._font_pequena
        self.data_label['text'] = 'Data*'
        self.data_label.pack()

        self.data_entry = Entry(self.main_frame)
        self.data_entry['width'] = 22
        self.data_entry['font'] = self._font_pequena
        self.data_entry.bind('<KeyRelease>', self._data_mask_key_released)
        self.data_entry.pack()

        self.butt_frame = Frame(self.window)
        self.butt_frame.pack()

        self.cancel_button = Button(self.butt_frame)
        self.cancel_button['font'] = self._font_pequena
        self.cancel_button['text'] = 'Cancelar'
        self.cancel_button['width'] = 8
        self.cancel_button['bg'] = '#d93a05'
        self.cancel_button['fg'] = '#ffffff'
        self.cancel_button['command'] = self._cancel_button_op
        self.cancel_button.pack(side=LEFT, padx=5, pady=15)

        self.create_button = Button(self.butt_frame)
        self.create_button['font'] = self._font_pequena
        self.create_button['text'] = 'Cadastrar'
        self.create_button['width'] = 8
        self.create_button['bg'] = '#002b36'
        self.create_button['fg'] = '#ffffff'
        self.create_button['command'] = self._create_button_op
        self.create_button.pack(side=LEFT, padx=5, pady=15)

        self.window.mainloop()

    def _data_mask_key_released(self, evt):
        """Mascara para data. Define em dd/mm/aaaa.

        Args:
            evt (event): <KeyRelease>
        """
        text = self.data_entry.get()
        try:
            if text.__len__() <= 2:
                int(text)
                text += '/' if len(text) == 2 else ''
            elif text.__len__() < 6:
                int(text[3:])
                text += '/' if len(text) == 5 else ''
            elif text.__len__() <= 10:
                int(text[6:])
            else:
                text = text[:10]
        except ValueError:
            text = text[:-1]
        finally:
            self.data_entry.delete(0, 'end')
            self.data_entry.insert(0, text)

    def _cancel_button_op(self) -> None:
        """Cancelar operação.
        """
        self.window.destroy()

    def _create_button_op(self) -> None:
        """Registrar Login operação.
        """
        if self.data_entry.get().__len__() < 10:
            messagebox.showwarning(
                title='Problema com data', message='Informação de data incompleta!')
            self.window.destroy()
            return
        self._login.nome = self.site_entry.get()
        self._login.link = self.link_entry.get()
        self._login.user = self.user_entry.get()
        self._login.email = self.email_entry.get()
        self._login.passw = self.senha_entry.get()
        self._login.data.dia = int(self.data_entry.get()[: 2])
        self._login.data.mes = int(self.data_entry.get()[3: 5])
        self._login.data.ano = int(self.data_entry.get()[6:])
        # tentativa de registro na base de dados
        if Fac.facade().create_login(login=self._login):
            messagebox.showinfo(title='Login Registrado',
                                message=Msg.message().mesg)
            self.window.destroy()
        else:
            messagebox.showerror(title='Login Não Registrado',
                                 message=Msg.message().mesg)
            self.window.destroy()
