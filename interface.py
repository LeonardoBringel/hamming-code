from tkinter import Canvas, StringVar, Tk

from hamming import *
from interface_utils import *


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.title('Hamming Code')
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')

        self.canvas = Canvas(self, width=400, height=300, relief='raised')
        self.canvas.pack()

        self.input_text = StringVar()
        self.input_text.trace('w', self.button_state_controller)

        self.label_text = StringVar()
        self.output_text = StringVar()

        title_font = ('Bahnschrift', 16, 'bold', 'underline')
        text_font = ('Bahnschrift', 14)
        button_font = ('bahnschrift', 12, 'bold')

        validate_command = (self.register(self.validate_input), '%P')

        create_label(self.canvas, 'Hamming Code', title_font, 200, 25)

        create_label(self.canvas, 'Enter the data bits: ', text_font, 200, 90)
        self.entry_input = create_entry(self.canvas, self.input_text, text_font, 200, 130, validate_command)

        self.button_encode = create_button(self.canvas, 'Encode', self.get_hamming_code, button_font, 160, 170)
        self.button_decode = create_button(self.canvas, 'Decode', self.get_hamming_decode, button_font, 240, 170)

        create_label(self.canvas, self.label_text, text_font, 200, 210)
        self.entry_output = create_entry(self.canvas, self.output_text, text_font, 200, 250)

    def get_hamming_code(self):
        self.label_text.set('Generated data: ')
        self.get_answer(True)

    def get_hamming_decode(self):
        self.label_text.set('Decoded data: ')
        self.get_answer(False)

    def get_answer(self, encode=True):
        bits = self.entry_input.get()
        bits = [int(bit) for bit in bits]

        result = hamming_code(bits) if encode else hamming_decode(bits)
        result = ''.join(str(bit) for bit in result)
        self.output_text.set(result)

    @staticmethod
    def validate_input(value):
        if len(value) != 0:
            value = value[-1]
        return True if value == '1' or value == '0' or value == '' else False

    def button_state_controller(self, *_):
        if len(self.input_text.get()) > 0:
            self.button_encode.config(state='normal')
            self.button_decode.config(state='normal')
        else:
            self.button_encode.config(state='disabled')
            self.button_decode.config(state='disabled')
