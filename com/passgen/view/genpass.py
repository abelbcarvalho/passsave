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

        # variaveis que mostra se os checkbuttons
        # foram selecionados
        self.num_sel = self.up_sel = self.low_sel = False
        self.sim_1 = self.sim_2 = self.sim_3 = False

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

        self.numeros_chk = Checkbutton(
            self.main_frame,
            text="Números",
        )
        self.numeros_chk['font'] = self._font_pequena
        self.numeros_chk.bind('<Button-1>', self._select_num_on_off)
        self.numeros_chk.pack()

        self.letras_up_chk = Checkbutton(
            self.main_frame,
            text="Letras Maíusculas",
        )
        self.letras_up_chk['font'] = self._font_pequena
        self.letras_up_chk.bind('<Button-1>', self._select_let_up_on_off)
        self.letras_up_chk.pack()

        self.letras_low_chk = Checkbutton(
            self.main_frame,
            text="Letras Minúsculas",
        )
        self.letras_low_chk['font'] = self._font_pequena
        self.letras_low_chk.bind('<Button-1>', self._select_let_low_on_off)
        self.letras_low_chk.pack()

        self.simbolos_1_chk = Checkbutton(
            self.main_frame,
            text='Conjunto Simbólico 1',
        )
        self.simbolos_1_chk['font'] = self._font_pequena
        self.simbolos_1_chk.bind('<Button-1>', self._select_sim_1_on_off)
        self.simbolos_1_chk.pack()

        self.simbolos_2_chk = Checkbutton(
            self.main_frame,
            text='Conjunto Simbólico 2',
        )
        self.simbolos_2_chk['font'] = self._font_pequena
        self.simbolos_2_chk.bind('<Button-1>', self._select_sim_2_on_off)
        self.simbolos_2_chk.pack()

        self.simbolos_3_chk = Checkbutton(
            self.main_frame,
            text='Conjunto Simbólico 3',
        )
        self.simbolos_3_chk['font'] = self._font_pequena
        self.simbolos_3_chk.bind('<Button-1>', self._select_sim_3_on_off)
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

    # metodos de seleciona ou não

    def _select_num_on_off(self, evt) -> None:
        """Seleciona ou não checkbutton numeros.

        Args:
            evt (mouse): <Button-1>
        """
        if not self.num_sel:
            self.numeros_chk.deselect()
            self.num_sel = True
        else:
            self.num_sel = False
            self.numeros_chk.select()

    def _select_let_up_on_off(self, evt) -> None:
        """Seleciona ou não checkbutton letras maiusculas.

        Args:
            evt (mouse): <Button-1>
        """
        if not self.up_sel:
            self.letras_up_chk.deselect()
            self.up_sel = True
        else:
            self.up_sel = False
            self.letras_up_chk.select()

    def _select_let_low_on_off(self, evt) -> None:
        """Seleciona ou não checkbutton letras minusculas.

        Args:
            evt (mouse): <Button-1>
        """
        if not self.low_sel:
            self.low_sel = True
            self.letras_low_chk.deselect()
        else:
            self.low_sel = False
            self.letras_low_chk.select()

    def _select_sim_1_on_off(self, evt) -> None:
        """Seleciona ou não checkbutton simbolos 1.

        Args:
            evt (mouse): <Button-1>
        """
        if not self.sim_1:
            self.sim_1 = True
            self.simbolos_1_chk.deselect()
        else:
            self.sim_1 = False
            self.simbolos_1_chk.select()

    def _select_sim_2_on_off(self, evt) -> None:
        """Seleciona ou não checkbutton simbolos 2.

        Args:
            evt (mouse): <Button-1>
        """
        if not self.sim_2:
            self.sim_2 = True
            self.simbolos_2_chk.deselect()
        else:
            self.sim_2 = False
            self.simbolos_2_chk.select()

    def _select_sim_3_on_off(self, evt) -> None:
        """Seleciona ou não checkbutton simbolos 3.

        Args:
            evt (mouse): <Button-1>
        """
        if not self.sim_3:
            self.sim_3 = True
            self.simbolos_3_chk.deselect()
        else:
            self.sim_3 = False
            self.simbolos_3_chk.select()

    def _gerar_senha(self, evt) -> None:
        """Metodo que representa a ação do butão
        gerar senha.

        Args:
            evt (event): <Button-1>
        """
        self.password.size = int(self.size_spin.get())
        self.password.numbers = self.num_sel
        self.password.upcase = self.up_sel
        self.password.lowcase = self.low_sel
        self.password.symbol_1 = self.sim_1
        self.password.symbol_2 = self.sim_2
        self.password.symbol_3 = self.sim_3
        self.senha_entry.delete(0, 'end')
        self.senha_entry.insert(
            0, Fac.facade().generate_password(passgen=self.password))
