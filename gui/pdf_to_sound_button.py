import tkinter as tk
from tkinter import filedialog
from .language_selection_window import LanguageSelectionWindow

class PdfToSoundButton(tk.Button):
    def __init__(self, root, progress, app_root):
        super().__init__(root, text="Convert PDF to Sound", command=self.open_pdf_to_sound)
        self.progress = progress  # Store the progress bar
        self.app_root = app_root  # Store the root window

    def open_pdf_to_sound(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            # Pass the progress bar and root window to LanguageSelectionWindow
            lang_window = LanguageSelectionWindow(self.master, file_path, self.progress, self.app_root)
            lang_window.open_window()