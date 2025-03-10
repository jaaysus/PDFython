import tkinter as tk
from tkinter import filedialog, messagebox
from core.txt_to_pdf import convert_txt_to_pdf

class TxtToPdfButton(tk.Button):
    def __init__(self, root):
        super().__init__(root, text="Convert TXT to PDF", command=self.convert_txt)

    def convert_txt(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if save_path:
                try:
                    convert_txt_to_pdf(file_path, save_path)
                    messagebox.showinfo("Success", "TXT file converted to PDF successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to convert TXT to PDF: {e}")
