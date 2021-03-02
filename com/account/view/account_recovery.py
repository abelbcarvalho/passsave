from tkinter import messagebox
from tkinter import Tk, Frame, Label, Entry, Button
from tkinter.constants import LEFT
from com.account.model.account import Account
from core.singleton.sing_message import SingMessage as Msg
from core.singleton.sing_facade import SingFacade as Fac


class AccountRecovery:
    """Essa cria a tela para recuperar a senha.

    Author:
        abelbcarvalho
    """
    _font_default = ('Courier 10 Pitch', 17)
    _font_pequena = (_font_default[0], 12)

    def __init__(self) -> None:
        """Nova tela para recuperação de senha.
        """
        self.window = Tk()
        self.window.minsize(width=512, height=470)
        self.window.title('PassSave - Salve Seus Logins')

        # frame title
        self.frame_title = Frame(self.window)
        self.frame_title.pack(pady=50)

        self.label_title = Label(self.frame_title)
        self.label_title['font'] = self._font_default
        self.label_title['text'] = 'PassSave - Recupera Senha'
        self.label_title.pack()

        # user/email -----------------------------------------
        self.frame_user = Frame(self.window)
        self.frame_user.pack(pady=7)

        # label email/user
        self.label_user = Label(self.frame_user)
        self.label_user['font'] = self._font_pequena
        self.label_user['text'] = 'Usuário/E-Mail'
        self.label_user.pack(side=LEFT, padx=7)

        # entry email/user
        self.entry_user = Entry(self.frame_user)
        self.entry_user['font'] = self._font_pequena
        self.entry_user['width'] = 25
        self.entry_user.pack(side=LEFT)

        # celular ------------------------------------
        self.frame_tell = Frame(self.window)
        self.frame_tell.pack(pady=7)

        # label celular
        self.label_tell = Label(self.frame_tell)
        self.label_tell['font'] = self._font_pequena
        self.label_tell['text'] = 'Telefone Celular'
        self.label_tell.pack(side=LEFT, padx=7)

        # entry celular  # need mask
        self.entry_tell = Entry(self.frame_tell)
        self.entry_tell['font'] = self._font_pequena
        self.entry_tell['width'] = 23
        self.entry_tell.pack(side=LEFT)

        # senha -----------------------------------
        self.frame_senha = Frame(self.window)
        self.frame_senha.pack(pady=7)

        self.label_senha = Label(self.frame_senha)
        self.label_senha['font'] = self._font_pequena
        self.label_senha['text'] = 'Senha'
        self.label_senha.pack(side=LEFT, padx=7)

        # entry senha  # need mask
        self.entry_senha = Entry(self.frame_senha)
        self.entry_senha['font'] = self._font_pequena
        self.entry_senha['width'] = 12
        self.entry_senha.pack(side=LEFT)

        self.label_confirm = Label(self.frame_senha)
        self.label_confirm['font'] = self._font_pequena
        self.label_confirm['text'] = 'Confirme'
        self.label_confirm.pack(side=LEFT, padx=7)

        # entry confirme
        self.entry_confirm = Entry(self.frame_senha)
        self.entry_confirm['font'] = self._font_pequena
        self.entry_confirm['width'] = 12
        self.entry_confirm.pack(side=LEFT)

        # link para tela de criar conta
        self.frame_create = Frame(self.window)
        self.frame_create.pack(pady=7)

        self.label_create = Label(self.frame_create)
        self.label_create['font'] = self._font_pequena
        self.label_create['text'] = 'Não Registrado? Crie uma Conta'
        self.label_create.bind('<Button-1>', self._go_to_create)
        self.label_create.bind('<Enter>', self._change_color_create)
        self.label_create.bind('<Leave>', self._revert_color_create)
        self.label_create.pack()

        # buttons --------------------------------------
        self.frame_butt = Frame(self.window)
        self.frame_butt.pack(side=LEFT, padx=109)

        # mudar senha
        self.butt_update = Button(self.frame_butt)
        self.butt_update['font'] = self._font_pequena
        self.butt_update['text'] = 'Atualizar'
        self.butt_update['bg'] = '#1454a8'
        self.butt_update['fg'] = '#ffffff'
        self.butt_update['width'] = 10
        self.butt_update.bind('<Button-1>', self._atualizando)
        self.butt_update.pack(side=LEFT, padx=7)

        # entrar
        self.butt_entrar = Button(self.frame_butt)
        self.butt_entrar['font'] = self._font_pequena
        self.butt_entrar['text'] = 'Entrar'
        self.butt_entrar['bg'] = '#ad0f03'
        self.butt_entrar['fg'] = '#ffffff'
        self.butt_entrar['command'] = self._back_to_entrar
        self.butt_entrar['width'] = 10
        self.butt_entrar.pack(side=LEFT, padx=7)

        # mostra janela
        self.window.mainloop()

    def _atualizando(self, evt):
        """Tentando atualizar senha.

        Args:
            evt (event): <Button-1>
        """
        if not self.entry_senha.get() == self.entry_confirm.get():
            messagebox.showerror(message='Erro: Senhas Diferentes.')
        else:
            account = Account()
            account.user = self.entry_user.get()
            account.passw = self.entry_senha.get()
            account.mobile = self.entry_tell.get()
            if Fac.facade().recovery_account(account=account):
                messagebox.showinfo(message=Msg.message().mesg)
            else:
                messagebox.showerror(message=Msg.message().mesg)

    def _back_to_entrar(self):
        """Volta para tela entrar.

        Returns:
            AccountAccess: instancia.
        """
        self.window.destroy()
        from com.account.view.account_access import AccountAccess
        return AccountAccess()

    def _change_color_create(self, evt) -> None:
        """Muda cor de label create.

        Args:
            evt (event): <Enter>
        """
        self.label_create['fg'] = '#ab0f0f'

    def _revert_color_create(self, evt) -> None:
        """Revert cor de label create.

        Args:
            evt (event): <Leave>
        """
        self.label_create['fg'] = '#000000'

    def _go_to_create(self, evt):
        """Esse metodo chava a tela de criar conta.

        Args:
            evt (event): <Button-1>

        Returns:
            AccountCreate: instancia.
        """
        self.window.destroy()
        from com.account.view.account_create import AccountCreate
        return AccountCreate()
