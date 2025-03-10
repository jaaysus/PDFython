import tkinter as tk
from tkinter import filedialog, messagebox
from core.pdf_text_extractor import extract_text_from_pdf

class ExtractTextButton(tk.Button):
    def __init__(self, root):
        super().__init__(root, text="Extract Text from PDF", command=self.extract_text)

    def extract_text(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if save_path:
                try:
                    extract_text_from_pdf(file_path, save_path)
                    messagebox.showinfo("Success", "Text extracted from PDF successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to extract text from PDF: {e}")
