from hamming import *
from tkinter import *

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

entry_input = Entry(window)
entry_input.config(font=('Bahnschrift', 14))
canvas.create_window(200, 130, window=entry_input)

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
