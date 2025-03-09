from gui.app_window import AppWindow
import tkinter as tk


# class PDFythonApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("PDFython - PDF Management")
#         self.root.geometry("400x300")
#         self.create_widgets()

#     def create_widgets(self):
#         tk.Button(self.root, text="Convert TXT to PDF", command=self.convert_txt_to_pdf).pack(pady=5)
#         tk.Button(self.root, text="Convert Excel to PDF", command=self.convert_excel_to_pdf).pack(pady=5)
#         tk.Button(self.root, text="Extract Text from PDF", command=self.extract_text_from_pdf).pack(pady=5)
#         tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=10)

#     def convert_txt_to_pdf(self):
#         file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
#         if not file_path:
#             return

#         save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
#         if not save_path:
#             return

#         try:
#             convert_txt_to_pdf(file_path, save_path)
#             messagebox.showinfo("Success", "TXT converted to PDF successfully!")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to convert TXT: {e}")

#     def convert_excel_to_pdf(self):
#         file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
#         if not file_path:
#             return

#         save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
#         if not save_path:
#             return

#         try:
#             convert_excel_to_pdf(file_path, save_path)
#             messagebox.showinfo("Success", "Excel converted to PDF successfully!")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to convert Excel: {e}")

#     def extract_text_from_pdf(self):
#         file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
#         if not file_path:
#             return

#         save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
#         if save_path:
#             try:
#                 extract_text_from_pdf(file_path, save_path)
#                 messagebox.showinfo("Success", "Text extracted and saved!")
#             except Exception as e:
#                 messagebox.showerror("Error", f"Failed to extract text: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = AppWindow(root)
    root.mainloop()
