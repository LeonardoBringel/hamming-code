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

window.mainloop()
