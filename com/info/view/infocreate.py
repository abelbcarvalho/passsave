from tkinter import messagebox
from tkinter import Tk, Frame, Label, Entry, Button
from tkinter.constants import LEFT
from com.info.model.info import Info
from core.singleton.sing_facade import SingFacade as Fac
from core.singleton.sing_message import SingMessage as Msg


class InfoCreate:
    """Tela de criação de Info.

    Author:
        abelbcarvalho
    """

    _font_default = ('Courier 10 Pitch', 17)
    _font_pequena = (_font_default[0], 12)

    def __init__(self, info=Info()):
        """Nova tela para criar Info.
        """
        self._info = info

        self.window = Tk()
        self.window.minsize(512, 300)
        self.window.maxsize(512, 300)
        self.window.title('PassSave - Inserir informação extra')

        self.title_frame = Frame(self.window)
        self.title_frame.pack(pady=10)

        self.title_label = Label(self.title_frame)
        self.title_label['font'] = self._font_default
        self.title_label['text'] = 'Registre Informação Extra'
        self.title_label.pack()

        self.id_label = Label(self.title_frame)
        self.id_label['font'] = self._font_pequena
        self.id_label['text'] = 'ID Login:'
        self.id_label.pack(side=LEFT)

        self.id_log_label = Label(self.title_frame)
        self.id_log_label['font'] = self._font_pequena
        self.id_log_label['text'] = f'{self._info.fk}'
        self.id_log_label['bg'] = '#ffff00'
        self.id_log_label.pack(side=LEFT)

        self.main_frame = Frame(self.window)
        self.main_frame.pack()

        self.comment_label = Label(self.main_frame)
        self.comment_label['font'] = self._font_pequena
        self.comment_label['text'] = 'Comentário*'
        self.comment_label.pack()

        self.comment_entry = Entry(self.main_frame)
        self.comment_entry['width'] = 40
        self.comment_entry['font'] = self._font_pequena
        self.comment_entry.pack()

        self.token_label = Label(self.main_frame)
        self.token_label['font'] = self._font_pequena
        self.token_label['text'] = 'Informação Adicional*'
        self.token_label.pack()

        self.token_entry = Entry(self.main_frame)
        self.token_entry['width'] = 40
        self.token_entry['font'] = self._font_pequena
        self.token_entry.pack()

        self.data_label = Label(self.main_frame)
        self.data_label['font'] = self._font_pequena
        self.data_label['text'] = 'Data*'
        self.data_label.pack()

        self.data_entry = Entry(self.main_frame)
        self.data_entry['width'] = 40
        self.data_entry['font'] = self._font_pequena
        self.data_entry.bind('<KeyRelease>', self._data_mask_key_released)
        self.data_entry.pack()

        self.butt_frame = Frame(self.window)
        self.butt_frame.pack()

        self.butt_cancel = Button(self.butt_frame)
        self.butt_cancel['width'] = 10
        self.butt_cancel['font'] = self._font_pequena
        self.butt_cancel['text'] = 'Cancelar'
        self.butt_cancel['bg'] = '#ad0f03'
        self.butt_cancel['fg'] = '#ffffff'
        self.butt_cancel['command'] = self._cancel_operation
        self.butt_cancel.pack(side=LEFT, padx=10, pady=20)

        self.butt_create = Button(self.butt_frame)
        self.butt_create['width'] = 10
        self.butt_create['font'] = self._font_pequena
        self.butt_create['text'] = 'Cadastrar'
        self.butt_create['bg'] = '#046910'
        self.butt_create['fg'] = '#ffffff'
        self.butt_create['command'] = self._create_operation
        self.butt_create.pack(side=LEFT, padx=10, pady=20)

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

    def _cancel_operation(self) -> None:
        """Botão Cancelar, fechar janela.
        """
        self.window.destroy()

    def _create_operation(self) -> None:
        """Botão Cadastrar, registro de info.
        """
        if self.data_entry.get().__len__() < 10:
            messagebox.showwarning(
                title='Problema com data',
                message='Informação de Data Incompleta',
            )
            self.window.destroy()
            return
        self._info.comment = self.comment_entry.get()
        self._info.inform = self.token_entry.get()
        self._info.data.dia = int(self.data_entry.get()[: 2])
        self._info.data.mes = int(self.data_entry.get()[3: 5])
        self._info.data.ano = int(self.data_entry.get()[6: ])
        # tentativa de registro na base de dados
        if Fac.facade().create_info(info=self._info):
            messagebox.showinfo(title='Info Registrado',
                                message=Msg.message().mesg)
            self.window.destroy()
        else:
            messagebox.showerror(title='Info Não Registrado',
                                 message=Msg.message().mesg)
            self.window.destroy()
