from tkinter import Tk, Frame, Label, Entry, Button
from tkinter import Checkbutton, Spinbox
from com.passgen.model.passgen import PassGen
from core.singleton.sing_facade import SingFacade as Fac


class GenPass:
    """Interface Gráfica para gerador de senhas.

    Author:
        abelbcarvalho
    """

    _font_default = ('Courier 10 Pitch', 17)
    _font_pequena = (_font_default[0], 12)

    def __init__(self):
        """Novo Gerador de Senhas.
        """
        self.window = Tk()
        self.password = PassGen()
        self.window.title('Gerador de Senhas')
        self.window.minsize(512, 370)
        self.window.maxsize(512, 370)

        self.main_frame = Frame(self.window)
        self.main_frame.pack()

        self.title_label = Label(self.main_frame)
        self.title_label['font'] = self._font_default
        self.title_label['text'] = 'Escolha os atributos e gere a senha'
        self.title_label.pack(pady=10)

        self.size_label = Label(self.main_frame)
        self.size_label['font'] = self._font_pequena
        self.size_label['text'] = 'Selecione o Tamanho'
        self.size_label.pack()

        self.size_spin = Spinbox(self.main_frame)
        self.size_spin['font'] = self._font_pequena
        self.size_spin['values'] = tuple(i for i in range(1, 101))
        self.size_spin['width'] = 25
        self.size_spin.pack()

        from tkinter import IntVar
        self._num_var = IntVar()
        self._let_up = IntVar()
        self._let_low = IntVar()
        self._sim_1 = IntVar()
        self._sim_2 = IntVar()
        self._sim_3 = IntVar()

        self.numeros_chk = Checkbutton(
            self.main_frame,
            text="Números",
            variable=self._num_var
        )
        self.numeros_chk['font'] = self._font_pequena
        self.numeros_chk.pack()

        self.letras_up_chk = Checkbutton(
            self.main_frame,
            text="Letras Maíusculas",
            variable=self._let_up
        )
        self.letras_up_chk['font'] = self._font_pequena
        self.letras_up_chk.pack()

        self.letras_low_chk = Checkbutton(
            self.main_frame,
            text="Letras Minúsculas",
            variable=self._let_low
        )
        self.letras_low_chk['font'] = self._font_pequena
        self.letras_low_chk.pack()

        self.simbolos_1_chk = Checkbutton(
            self.main_frame,
            text='Conjunto Simbólico 1',
            variable=self._sim_1
        )
        self.simbolos_1_chk['font'] = self._font_pequena
        self.simbolos_1_chk.pack()

        self.simbolos_2_chk = Checkbutton(
            self.main_frame,
            text='Conjunto Simbólico 2',
            variable=self._sim_2
        )
        self.simbolos_2_chk['font'] = self._font_pequena
        self.simbolos_2_chk.pack()

        self.simbolos_3_chk = Checkbutton(
            self.main_frame,
            text='Conjunto Simbólico 3',
            variable=self._sim_3
        )
        self.simbolos_3_chk['font'] = self._font_pequena
        self.simbolos_3_chk.pack()

        self.senha_entry = Entry(self.main_frame)
        self.senha_entry['font'] = self._font_pequena
        self.senha_entry['width'] = 40
        self.senha_entry.pack(pady=10)

        self.gen_button = Button(self.main_frame)
        self.gen_button['font'] = self._font_pequena
        self.gen_button['text'] = 'Gerar Senha'
        self.gen_button['width'] = 10
        self.gen_button['fg'] = '#ffffff'
        self.gen_button['bg'] = '#002b36'
        self.gen_button.bind('<Button-1>', self._gerar_senha)
        self.gen_button.pack(pady=20)

        self.window.mainloop()

    def _gerar_senha(self, evt) -> None:
        """Metodo que representa a ação do butão
        gerar senha.

        Args:
            evt (event): <Button-1>
        """
        self.password.size = int(self.size_spin.get())
        self.password.numbers = True if self._num_var.get() == 1 else False
        self.password.upcase = True if self._let_up.get() == 1 else False
        self.password.lowcase = True if self._let_low.get() == 1 else False
        self.password.symbol_1 = True if self._sim_1.get() == 1 else False
        self.password.symbol_2 = True if self._sim_2.get() == 1 else False
        self.password.symbol_3 = True if self._sim_3.get() == 1 else False
        self.senha_entry.delete(0, 'end')
        self.senha_entry.insert(
            0, Fac.facade().generate_password(passgen=self.password))
