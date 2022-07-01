from hamming import *
from tkinter import *
from interface_utils import *


def get_hamming_code():
    label_text.set('Generated data: ')
    get_answer(True)


def get_hamming_decode():
    label_text.set('Decoded data: ')
    get_answer(False)


def get_answer(encode=True):
    bits = entry_input.get()
    bits = [int(bit) for bit in bits]

    result = hamming_code(bits) if encode else hamming_decode(bits)
    result = ''.join(str(bit) for bit in result)
    output_text.set(result)


def validate_input(value):
    if len(value) != 0:
        value = value[-1]

    return True if value == '1' or value == '0' or value == '' else False


def button_state_controller(*_):
    if len(input_text.get()) > 0:
        button_encode.config(state='normal')
        button_decode.config(state='normal')
    else:
        button_encode.config(state='disabled')
        button_decode.config(state='disabled')


window = Tk()
window.title('Hamming Code')
window.resizable(False, False)
window.eval('tk::PlaceWindow . center')

canvas = Canvas(window, width=400, height=300, relief='raised')
canvas.pack()

create_label(canvas, 'Hamming Code', ('Bahnschrift', 16, 'bold', 'underline'), 200, 25)
create_label(canvas, 'Enter the data bits: ', ('Bahnschrift', 14), 200, 90)

validate_command = (window.register(validate_input), '%P')

input_text = StringVar()
input_text.trace('w', button_state_controller)

entry_input = create_entry(canvas, input_text, ('Bahnschrift', 14), 200, 130, validate_command)

button_encode = create_button(canvas, 'Encode', get_hamming_code, ('bahnschrift', 12, 'bold'), 160, 170)
button_decode = create_button(canvas, 'Decode', get_hamming_decode, ('bahnschrift', 12, 'bold'), 240, 170)

label_text = StringVar()
output_text = StringVar()

create_label(canvas, label_text, ('Bahnschrift', 14), 200, 210)
entry_output = create_entry(canvas, output_text, ('Bahnschrift', 14), 200, 250)

window.mainloop()
