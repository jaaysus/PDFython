import tkinter as tk
from tkinter import filedialog, messagebox
from core.txt_to_pdf import convert_txt_to_pdf
from core.excel_to_pdf import convert_excel_to_pdf
from core.pdf_text_extractor import extract_text_from_pdf
from core.pdf_to_word import convert_pdf_to_word
from core.pdf_to_sound import convert_pdf_to_sound  

class AppWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("PDFython - PDF Management")
        self.root.geometry("400x300")

        # Buttons
        self.txt_to_pdf_btn = tk.Button(root, text="Convert TXT to PDF", command=self.convert_txt)
        self.txt_to_pdf_btn.pack(pady=5)

        self.excel_to_pdf_btn = tk.Button(root, text="Convert Excel to PDF", command=self.convert_excel)
        self.excel_to_pdf_btn.pack(pady=5)

        self.extract_text_btn = tk.Button(root, text="Extract Text from PDF", command=self.extract_text)
        self.extract_text_btn.pack(pady=5)

        self.pdf_to_word_btn = tk.Button(root, text="Convert PDF to Word", command=self.convert_pdf_to_word)
        self.pdf_to_word_btn.pack(pady=5)

        self.pdf_to_sound_btn = tk.Button(root, text="Convert PDF to Sound", command=self.open_pdf_to_sound)
        self.pdf_to_sound_btn.pack(pady=5)

        self.exit_btn = tk.Button(root, text="Exit", command=root.quit)
        self.exit_btn.pack(pady=5)

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

    def open_pdf_to_sound(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            try:
                audio_file = convert_pdf_to_sound(file_path)  
                messagebox.showinfo("Success", f"Audio file saved as {audio_file}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to convert PDF to sound: {e}")