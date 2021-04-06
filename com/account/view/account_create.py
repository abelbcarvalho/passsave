from tkinter import Tk, Frame, Entry, Label, Button
from tkinter import Checkbutton, messagebox
from tkinter.ttk import Combobox
from tkinter.constants import LEFT
from com.account.model.account import Account
from core.singleton.sing_message import SingMessage as Msg
from core.singleton.sing_facade import SingFacade as Fac


class AccountCreate:
    """Tela para criação de conta de usuário.

    Author:
        abelbcarvalho
    """

    _font_default = ('Courier 10 Pitch', 17)
    _font_pequena = (_font_default[0], 12)

    def __init__(self) -> None:
        """Tela Para Criar Nova Conta.
        """
        self.window = Tk()
        self.window.minsize(width=512, height=470)
        self.window.title('PassSave - Salve Seus Logins')
        # main frame
        self.main_frame = Frame(self.window)
        self.main_frame.pack(pady=50)

        self.label_title = Label(self.main_frame)
        self.label_title['font'] = self._font_default
        self.label_title['text'] = 'PassSave - Novo Cadastro'
        self.label_title.pack()

        # label nome e sexo
        self.name_frame = Frame(self.window)
        self.name_frame.pack(pady=7)

        self.name_label = Label(self.name_frame)
        self.name_label['text'] = 'Nome'
        self.name_label['font'] = self._font_pequena
        self.name_label.pack(side=LEFT)

        self.name_entry = Entry(self.name_frame)
        self.name_entry['width'] = 23
        self.name_entry['font'] = self._font_pequena
        self.name_entry.pack(side=LEFT)

        self.label_sexo = Label(self.name_frame)
        self.label_sexo['text'] = 'Sexo'
        self.label_sexo['font'] = self._font_pequena
        self.label_sexo.pack(side=LEFT)

        self.comb_sexo = Combobox(self.name_frame)
        self.comb_sexo['values'] = ('not say', 'masculino', 'feminino')
        self.comb_sexo['width'] = 10
        self.comb_sexo['font'] = self._font_pequena
        self.comb_sexo.current(0)
        self.comb_sexo.pack(side=LEFT)

        # ---- usuario e data de nascimento
        self.user_frame = Frame(self.window)
        self.user_frame.pack(pady=7)

        self.user_label = Label(self.user_frame)
        self.user_label['font'] = self._font_pequena
        self.user_label['text'] = 'Usuário'if self.data_entry.get().__len__() < 10:
            messagebox.showwarning(
                title='Problema com data', message='Informação de data incompleta!')
            return
        self.user_label.pack(side=LEFT)

        self.user_entry = Entry(self.user_frame)
        self.user_entry['font'] = self._font_pequena
        self.user_entry['width'] = 20
        self.user_entry.pack(side=LEFT)

        self.data_label = Label(self.user_frame)
        self.data_label['font'] = self._font_pequena
        self.data_label['text'] = 'Nasc.'
        self.data_label.pack(side=LEFT)

        # data
        self.data_entry = Entry(self.user_frame)
        self.data_entry['font'] = self._font_pequena
        self.data_entry['width'] = 10
        self.data_entry.bind('<KeyRelease>', self._data_mask_key_released)
        self.data_entry.pack(side=LEFT)

        # email ---
        self.email_frame = Frame(self.window)
        self.email_frame.pack(pady=7)

        self.label_email = Label(self.email_frame)
        self.label_email['text'] = 'E-Mail'
        self.label_email['font'] = self._font_pequena
        self.label_email.pack(side=LEFT)

        self.email_entry = Entry(self.email_frame)
        self.email_entry['font'] = self._font_pequena
        self.email_entry['width'] = 37
        self.email_entry.pack(side=LEFT)

        # senha e celular
        self.senha_frame = Frame()
        self.senha_frame.pack(pady=7)

        self.label_senha = Label(self.senha_frame)
        self.label_senha['font'] = self._font_pequena
        self.label_senha['text'] = 'Senha'
        self.label_senha.pack(side=LEFT)

        # senha  # need mask
        self.senha_entry = Entry(self.senha_frame, show='*')
        self.senha_entry['width'] = 19
        self.senha_entry['font'] = self._font_pequena
        self.senha_entry.pack(side=LEFT)

        self.label_cel = Label(self.senha_frame)
        self.label_cel['text'] = 'Cel.'
        self.label_cel['font'] = self._font_pequena
        self.label_cel.pack(side=LEFT)

        # celular  # need mask
        self.cel_entry = Entry(self.senha_frame)
        self.cel_entry['width'] = 14
        self.cel_entry['font'] = self._font_pequena
        self.cel_entry.bind('<KeyRelease>', self._mobile_mask_key_release)
        self.cel_entry.pack(side=LEFT)

        # checkbutton mostrar senha ---------------
        self.chk_frame = Frame(self.window)
        self.chk_frame.pack()

        # check button
        from tkinter import IntVar
        self._show_pass = IntVar()
        self.chk_show = Checkbutton(
            self.chk_frame,
            text='Mostrar Senha',
            variable=self._show_pass
        )
        self.chk_show['font'] = self._font_pequena
        self.chk_show.bind('<Button-1>', self._mostra_senha)
        self.chk_show.pack()

        # buttons ---------------------------------
        self.butt_frame = Frame(self.window)
        self.butt_frame.pack(side=LEFT, padx=109)

        # cadastrar
        self.butt_create = Button(self.butt_frame)
        self.butt_create['font'] = self._font_pequena
        self.butt_create['text'] = 'Cadastrar'
        self.butt_create['bg'] = '#046910'
        self.butt_create['fg'] = '#ffffff'
        self.butt_create['width'] = 10
        self.butt_create.bind('<Button-1>', self._registrando)
        self.butt_create.pack(side=LEFT, padx=7)

        # entrar
        self.butt_entrar = Button(self.butt_frame)
        self.butt_entrar['font'] = self._font_pequena
        self.butt_entrar['text'] = 'Entrar'
        self.butt_entrar['bg'] = '#ad0f03'
        self.butt_entrar['fg'] = '#ffffff'
        self.butt_entrar['width'] = 10
        self.butt_entrar['command'] = self._back_to_access
        self.butt_entrar.pack(side=LEFT, padx=7)

        # mostra janela
        self.window.mainloop()

    def _registrando(self, evt):
        """Registrando conta.

        Args:
            evt (event): <Button-'>
        """
        if self.data_entry.get().__len__() < 10:
            messagebox.showwarning(
                title='Problema com data', message='Informação de data incompleta!')
            return
        account = Account()
        account.nome = self.name_entry.get()
        account.sexo = self.comb_sexo.get()
        account.nasc.dia = int(self.data_entry.get()[: 2])
        account.nasc.mes = int(self.data_entry.get()[3: 5])
        account.nasc.ano = int(self.data_entry.get()[6:])
        account.user = self.user_entry.get()
        account.email = self.email_entry.get()
        account.passw = self.senha_entry.get()
        account.mobile = self.cel_entry.get()
        # somente será feito o restante após adicionada as mascaras de texto
        if Fac.facade().create_account(account=account):
            messagebox.showinfo(title='Conta Registrada',
                                message=Msg.message().mesg)
        else:
            messagebox.showerror(title='Conta Não Registrada',
                                 message=Msg.message().mesg)

    def _back_to_access(self):
        """Esse metodo retorna para a tela
        de acesso ao aplicativo.

        Returns:
            AccountAccess: instancia.
        """
        from com.account.view.account_access import AccountAccess
        self.window.destroy()
        return AccountAccess()

    def _mobile_mask_key_release(self, evt):
        """Mascara para mobile. Define em
        +0011222222222.

        Args:
            evt (event): <KeyRelease>
        """
        text = self.cel_entry.get()
        try:
            if text.__len__() == 1:
                if text == '+':
                    pass
                else:
                    int(text)
                    text = '+' + text
            elif text.__len__() < 15:
                int(text[1:])
            else:
                text = text[:14]
        except ValueError:
            text = text[:-1]
        finally:
            self.cel_entry.delete(0, 'end')
            self.cel_entry.insert(0, text)

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

    def _mostra_senha(self, evt):
        """Mostra a senha ou oculta ela a depender.

        Args:
            evt ('<Button-1>'): evento clique de mouse.
        """
        self.senha_entry['show'] = '' \
            if not self._show_pass.get() else '*'
