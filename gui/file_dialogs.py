from tkinter import filedialog

def open_file_dialog(file_types):
    return filedialog.askopenfilename(filetypes=file_types)

def save_file_dialog(default_ext, file_types):
    return filedialog.asksaveasfilename(defaultextension=default_ext, filetypes=file_types)
