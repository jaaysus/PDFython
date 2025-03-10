import tkinter as tk
from tkinter import filedialog, messagebox
from core.excel_to_pdf import convert_excel_to_pdf

class ExcelToPdfButton(tk.Button):
    def __init__(self, root):
        super().__init__(root, text="Convert Excel to PDF", command=self.convert_excel)

    def convert_excel(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if file_path:
            save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if save_path:
                try:
                    convert_excel_to_pdf(file_path, save_path)
                    messagebox.showinfo("Success", "Excel file converted to PDF successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to convert Excel to PDF: {e}")
