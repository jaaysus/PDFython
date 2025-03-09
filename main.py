import tkinter as tk
from tkinter import filedialog, messagebox
import pdfplumber
import openpyxl
import chardet
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class PDFythonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDFython - PDF Management")
        self.root.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        tk.Button(self.root, text="Convert TXT to PDF", command=self.convert_txt_to_pdf).pack(pady=5)
        tk.Button(self.root, text="Convert Excel to PDF", command=self.convert_excel_to_pdf).pack(pady=5)
        tk.Button(self.root, text="Extract Text from PDF", command=self.extract_text_from_pdf).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=10)

    def convert_txt_to_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if not file_path:
            return

        try:
            
            with open(file_path, "rb") as file:
                raw_data = file.read()
                result = chardet.detect(raw_data)  
                encoding = result["encoding"]

            
            with open(file_path, "r", encoding=encoding, errors="replace") as file:
                content = file.read()

            save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if not save_path:
                return

            
            c = canvas.Canvas(save_path, pagesize=letter)
            c.setFont("Helvetica", 12)

            
            y_position = 750  

            for line in content.splitlines():
                c.drawString(72, y_position, line)  
                y_position -= 14  

                
                if y_position < 72:
                    c.showPage()
                    c.setFont("Helvetica", 12)
                    y_position = 750

            c.save()
            messagebox.showinfo("Success", "TXT converted to PDF successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert TXT: {e}")

    def convert_excel_to_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if not file_path:
            return

        try:
            wb = openpyxl.load_workbook(file_path)
            ws = wb.active

            save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
            if not save_path:
                return

            
            c = canvas.Canvas(save_path, pagesize=letter)
            c.setFont("Helvetica", 12)

            
            y_position = 750
            for row in ws.iter_rows(values_only=True):
                line = " | ".join(str(cell) for cell in row)
                c.drawString(72, y_position, line)
                y_position -= 14

                if y_position < 72:
                    c.showPage()
                    c.setFont("Helvetica", 12)
                    y_position = 750

            c.save()
            messagebox.showinfo("Success", "Excel converted to PDF successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert Excel: {e}")

    def extract_text_from_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if not file_path:
            return

        try:
            extracted_text = ""
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    extracted_text += page.extract_text() + "\n"

            save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
            if save_path:
                with open(save_path, "w", encoding="utf-8") as file:
                    file.write(extracted_text)
                messagebox.showinfo("Success", "Text extracted and saved!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to extract text: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFythonApp(root)
    root.mainloop()
