import tkinter as tk
from tkinter import filedialog, messagebox
from .language_selection_window import LanguageSelectionWindow

class PdfToSoundButton(tk.Button):
    def __init__(self, root):
        super().__init__(root, text="Convert PDF to Sound", command=self.open_pdf_to_sound)

    def open_pdf_to_sound(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            lang_window = LanguageSelectionWindow(self.master, file_path)
            lang_window.open_window()
