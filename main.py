from hamming import *
from tkinter import *


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


window = Tk()
window.title('Hamming Code')
window.resizable(False, False)
window.eval('tk::PlaceWindow . center')

canvas = Canvas(window, width=400, height=300, relief='raised')
canvas.pack()

label = Label(window, text='Hamming Code', font=('Bahnschrift', 16, 'bold', 'underline'))
canvas.create_window(200, 25, window=label)

label = Label(window, text='Enter the data bits: ')
label.config(font=('Bahnschrift', 14))
canvas.create_window(200, 90, window=label)

validate_command = (window.register(validate_input), '%P')

entry_input = Entry(window, validate='all', validatecommand=validate_command)
entry_input.config(font=('Bahnschrift', 14))
canvas.create_window(200, 130, window=entry_input)

button_encode = Button(text='Encode', command=get_hamming_code, font=('bahnschrift', 12, 'bold'))
canvas.create_window(160, 170, window=button_encode)

button_decode = Button(text='Decode', command=get_hamming_decode, font=('bahnschrift', 12, 'bold'))
canvas.create_window(240, 170, window=button_decode)

label_text = StringVar()
label_text.set('')
output_text = StringVar()

label2 = Label(window, textvariable=label_text)
label2.config(font=('Bahnschrift', 14))
canvas.create_window(200, 210, window=label2)

entry_output = Entry(window)
entry_output.config(textvariable=output_text, state='readonly', font=('Bahnschrift', 14))
canvas.create_window(200, 250, window=entry_output)

window.mainloop()
