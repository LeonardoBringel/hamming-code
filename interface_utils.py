from tkinter import Button, Entry, Label


def create_label(canvas, text, custom_font, x, y):
    if isinstance(text, str):
        label = Label(text=text, font=custom_font)
    else:
        label = Label(textvariable=text, font=custom_font)
    canvas.create_window(x, y, window=label)
    return label


def create_button(canvas, text, command, custom_font, x, y):
    button = Button(text=text, state='disabled', command=command, font=custom_font)
    canvas.create_window(x, y, window=button)
    return button


def create_entry(canvas, text_variable, custom_font, x, y, validate_command=None):
    if validate_command is not None:
        entry = Entry(textvariable=text_variable, validate='all', validatecommand=validate_command, font=custom_font)
    else:
        entry = Entry(textvariable=text_variable, state='readonly', font=custom_font)
    canvas.create_window(x, y, window=entry)
    return entry
