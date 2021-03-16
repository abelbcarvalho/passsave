from tkinter import Button, Entry, Label, Tk
from tkinter import Frame, messagebox
from tkinter.constants import LEFT
from com.account.model.account import Account
from core.singleton.sing_message import SingMessage as Msg
from core.singleton.sing_facade import SingFacade as Fac


class AccountAccess:
    """Nessa classe é possivel ter as informações dispostas
    de modo a criar uma tela de interface gráfica com o tkinter,
    para que o usuário venha a ter acesso a sua conta.

    Author:
        abelbcarvalho
    """
    _font_default = ('Courier 10 Pitch', 17)
    _font_pequena = (_font_default[0], 12)

    def __init__(self) -> None:
        """Builder.
        :param self.window: Tk Object.
        """
        self.window = Tk()
        self.window.minsize(width=512, height=470)
        self.window.title('PassSave - Salve Seus Logins')
        # title
        self.main_frame = Frame(self.window)
        self.main_frame.pack(pady=50)

        self.wind_title = Label(self.main_frame)
        self.wind_title['font'] = self._font_default
        self.wind_title['text'] = 'PassSave - Entrando'
        self.wind_title.pack()

        # lable user/email
        self.user_frame = Frame(self.window)
        self.user_frame.pack()

        self.label_user = Label(self.user_frame)
        self.label_user['font'] = self._font_pequena
        self.label_user['text'] = 'Nome de Usuário/E-Mail'
        self.label_user.pack()

        # entry user/email
        self.user_entry = Entry(self.user_frame)
        self.user_entry['font'] = self._font_pequena
        self.user_entry['width'] = 35
        self.user_entry.pack()

        # label password
        self.pass_frame = Frame(self.window)
        self.pass_frame.pack(pady=30)

        self.label_pass = Label(self.pass_frame)
        self.label_pass['text'] = 'Digite Sua Senha'
        self.label_pass['font'] = self._font_pequena
        self.label_pass.pack()

        # entry password
        self.pass_entry = Entry(self.pass_frame, show='*')
        self.pass_entry['font'] = self._font_pequena
        self.pass_entry['width'] = 35
        self.pass_entry.pack()

        # label esqueceu senha
        self.label_recover = Label(self.pass_frame)
        self.label_recover['text'] = 'Recuperar Senha'
        self.label_recover['font'] = self._font_pequena
        self.label_recover.bind('<Leave>', self._change_color_out)
        self.label_recover.bind('<Enter>', self._change_color_enter)
        self.label_recover.bind('<Button-1>', self._go_to_recovery)
        self.label_recover.pack()

        # ---------------------------------------------
        self.butt_frame = Frame(self.window)
        self.butt_frame.pack(side=LEFT, padx=109)

        # entrar
        self.butt_entrar = Button(self.butt_frame)
        self.butt_entrar['font'] = self._font_pequena
        self.butt_entrar['text'] = 'Entrar'
        self.butt_entrar['bg'] = '#046910'
        self.butt_entrar['fg'] = '#ffffff'
        self.butt_entrar['width'] = 10
        self.butt_entrar.bind('<Button-1>', self._entrando)
        self.butt_entrar.pack(side=LEFT, padx=7)

        # criar conta
        self.butt_create = Button(self.butt_frame)
        self.butt_create['font'] = self._font_pequena
        self.butt_create['text'] = 'Cadastro'
        self.butt_create['bg'] = '#ad0f03'
        self.butt_create['fg'] = '#ffffff'
        self.butt_create['width'] = 10
        self.butt_create['command'] = self._go_to_create
        self.butt_create.pack(side=LEFT, padx=7)

        # mostra janela
        self.window.mainloop()

    def _entrando(self, evt):
        """Tentando fazer login no aplicativo.

        Args:
            evt (event): <Button-1>
        """
        account = Account()
        account.user = self.user_entry.get()
        account.email = self.user_entry.get()
        account.passw = self.pass_entry.get()  # need mask
        data = Fac.facade().read_account(
            user=account.user,
            email=account.email,
            passw=account.passw,
        )
        if not data:
            messagebox.showerror(message=Msg.message().mesg)
        else:
            data = data[0]
            messagebox.showinfo(message=Msg.message().mesg)

    def _go_to_create(self):
        """Ir para criar uma conta.

        Returns:
            AccountCreate: instancia.
        """
        self.window.destroy()
        from com.account.view.account_create import AccountCreate
        return AccountCreate()

    def _go_to_recovery(self, evt):
        """Chama a tela para mudança de senha
        e recuperação de acesso.

        Returns:
            AccountRecovery: instancia.
        """
        self.window.destroy()
        from com.account.view.account_recovery import AccountRecovery
        return AccountRecovery()

    def _change_color_enter(self, evt) -> None:
        """Mudando cor de texto do Label recover.

        Args:
            evt ([event): quando mouse entra sobre o texto.
        """
        self.label_recover['fg'] = '#054db3'

    def _change_color_out(self, evt) -> None:
        """Mudando cor de texto do Label recover.

        Args:
            evt ([event): quando mouse sai de sobre o texto.
        """
        self.label_recover['fg'] = '#000000'
