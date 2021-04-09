from com.account.model.account import Account
from tkinter import Checkbutton
from tkinter import Tk, Frame, Label, Entry, Button
from tkinter.ttk import Combobox
from tkinter.constants import LEFT, NORMAL, DISABLED


class Perfil:
    """Classe com o perfil de usuário do aplicativo.

    Author:
        abelbcarvalho
    """

    _font_default = ('Courier 10 Pitch', 17)
    _font_pequena = (_font_default[0], 12)

    def __init__(self, account=Account()):
        """Novo Perfil.
        """
        self._account = account
        self._editavel = False

        self.window = Tk()
        self.window.minsize(512,480)
        self.window.maxsize(512,480)
        self.window.title('PassSave - Perfil de Usuário')

        self.main_frame = Frame(self.window)
        self.main_frame.pack()

        self.title_label = Label(self.main_frame)
        self.title_label['font'] = self._font_default
        self.title_label['text'] = 'Perfil de Usuário PassSave'
        self.title_label.pack(pady=10)

        self.name_label = Label(self.main_frame)
        self.name_label['font'] = self._font_pequena
        self.name_label['text'] = 'Nome Completo'
        self.name_label.pack()

        self.name_entry = Entry(self.main_frame)
        self.name_entry['width'] = 40
        self.name_entry['font'] = self._font_pequena
        self.name_entry['state'] = DISABLED
        self.name_entry.pack()

        self.sexo_label = Label(self.main_frame)
        self.sexo_label['font'] = self._font_pequena
        self.sexo_label['text'] = 'Sexo'
        self.sexo_label.pack()

        self.sexo_combo = Combobox(self.main_frame)
        self.sexo_combo['values'] = ('not say', 'masculino', 'feminino')
        self.sexo_combo['width'] = 39
        self.sexo_combo['font'] = self._font_pequena
        self.sexo_combo['state'] = DISABLED
        self.sexo_combo.pack()

        self.nasc_label = Label(self.main_frame)
        self.nasc_label['font'] = self._font_pequena
        self.nasc_label['text'] = 'Data de Nascimento'
        self.nasc_label.pack()

        self.data_entry = Entry(self.main_frame)
        self.data_entry['font'] = self._font_pequena
        self.data_entry['width'] = 40
        self.data_entry.bind('<KeyRelease>', self._data_mask_key_released)
        self.data_entry['state'] = DISABLED
        self.data_entry.pack()

        self.user_label = Label(self.main_frame)
        self.user_label['font'] = self._font_pequena
        self.user_label['text'] = 'Nome de Usuário'
        self.user_label.pack()

        self.user_entry = Entry(self.main_frame)
        self.user_entry['width'] = 40
        self.user_entry['font'] = self._font_pequena
        self.user_entry['state'] = DISABLED
        self.user_entry.pack()

        self.email_label = Label(self.main_frame)
        self.email_label['font'] = self._font_pequena
        self.email_label['text'] = 'Endereço de E-Mail'
        self.email_label.pack()

        self.email_entry = Entry(self.main_frame)
        self.email_entry['width'] = 40
        self.email_entry['font'] = self._font_pequena
        self.email_entry['state'] = DISABLED
        self.email_entry.pack()

        self.senha_label = Label(self.main_frame)
        self.senha_label['font'] = self._font_pequena
        self.senha_label['text'] = 'Senha'
        self.senha_label.pack()
        
        self.senha_entry = Entry(self.main_frame)
        self.senha_entry['font'] = self._font_pequena
        self.senha_entry['width'] = 40
        self.senha_entry['state'] = DISABLED
        self.senha_entry.pack()

        self.mobile_label = Label(self.main_frame)
        self.mobile_label['font'] = self._font_pequena
        self.mobile_label['text'] = 'Telefone Celular'
        self.mobile_label.pack()

        self.mobile_entry = Entry(self.main_frame)
        self.mobile_entry['font'] = self._font_pequena
        self.mobile_entry['width'] = 40
        self.mobile_entry['state'] = DISABLED
        self.mobile_entry.bind('<KeyRelease>', self._mobile_mask_key_release)
        self.mobile_entry.pack()

        from tkinter import IntVar
        self._show_pass = IntVar()
        self.chk_show = Checkbutton(
            self.main_frame,
            text='Mostrar Senha',
            variable=self._show_pass
        )
        self.chk_show['font'] = self._font_pequena
        self.chk_show.bind('<Button-1>', self._mostra_senha)
        self.chk_show['state'] = DISABLED
        self.chk_show.pack()

        self.button_frame = Frame(self.window)
        self.button_frame.pack()

        self.edit_button = Button(self.button_frame)
        self.edit_button['bg'] = '#ad0f03'
        self.edit_button['fg'] = '#ffffff'
        self.edit_button['text'] = 'Não Editável'
        self.edit_button['font'] = self._font_pequena
        self.edit_button['width'] = 15
        self.edit_button.bind('<Button-1>', self._tornar_editavel)
        self.edit_button.pack(side=LEFT, pady=15, padx=10)

        self.update_button = Button(self.button_frame)
        self.update_button['bg'] = '#046910'
        self.update_button['fg'] = '#ffffff'
        self.update_button['text'] = 'Atualizar'
        self.update_button['font'] = self._font_pequena
        self.update_button['width'] = 15
        self.update_button['state'] = DISABLED
        self.update_button.pack(side=LEFT, pady=15, padx=10)

        self.window.mainloop()

    @property
    def editavel(self) -> bool:
        return self._editavel
    
    @editavel.setter
    def editavel(self, editavel: bool) -> None:
        self._editavel = editavel
    
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
    
    def _mobile_mask_key_release(self, evt):
        """Mascara para mobile. Define em
        +0011222222222.

        Args:
            evt (event): <KeyRelease>
        """
        text = self.mobile_entry.get()
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
            self.mobile_entry.delete(0, 'end')
            self.mobile_entry.insert(0, text)
    
    def _tornar_editavel(self, evt) -> None:
        """Esse metodo pode ou não tornar 
        os dados editáveis.

        Args:
            evt (mouse event): <Button-1>
        """
        if not self.editavel:
            self.name_entry['state'] = NORMAL
            self.sexo_combo['state'] = NORMAL
            self.update_button['state'] = NORMAL
            self.data_entry['state'] = NORMAL
            self.user_entry['state'] = NORMAL
            self.email_entry['state'] = NORMAL
            self.senha_entry['state'] = NORMAL
            self.mobile_entry['state'] = NORMAL
            self.chk_show['state'] = NORMAL
            self.edit_button['text'] = 'Editável'
            self.edit_button['bg'] = '#002b36'
            self.editavel = True
        else:
            self.name_entry['state'] = DISABLED
            self.sexo_combo['state'] = DISABLED
            self.update_button['state'] = DISABLED
            self.data_entry['state'] = DISABLED
            self.user_entry['state'] = DISABLED
            self.email_entry['state'] = DISABLED
            self.senha_entry['state'] = DISABLED
            self.mobile_entry['state'] = DISABLED
            self.chk_show['state'] = DISABLED
            self.edit_button['text'] = 'Não Editável'
            self.edit_button['bg'] = '#ad0f03'
            self.editavel = False
