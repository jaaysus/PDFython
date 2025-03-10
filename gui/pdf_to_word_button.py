import tkinter as tk
from tkinter import filedialog, messagebox
from core.pdf_to_word import convert_pdf_to_word

class PdfToWordButton(tk.Button):
    def __init__(self, root):
        super().__init__(root, text="Convert PDF to Word", command=self.convert_pdf_to_word)

    def convert_pdf_to_word(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            save_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Files", "*.docx")])
            if save_path:
                try:
                    convert_pdf_to_word(file_path, save_path)
                    messagebox.showinfo("Success", "PDF file converted to Word successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to convert PDF to Word: {e}")
