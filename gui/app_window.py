import tkinter as tk
from tkinter import ttk
from .txt_to_pdf_button import TxtToPdfButton
from .excel_to_pdf_button import ExcelToPdfButton
from .extract_text_button import ExtractTextButton
from .pdf_to_word_button import PdfToWordButton
from .pdf_to_sound_button import PdfToSoundButton

class AppWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("PDFython - PDF Management")
        self.root.geometry("400x350")  # Increased height to accommodate the progress bar

        # Buttons
        self.txt_to_pdf_btn = TxtToPdfButton(root)
        self.txt_to_pdf_btn.pack(pady=5)

        self.excel_to_pdf_btn = ExcelToPdfButton(root)
        self.excel_to_pdf_btn.pack(pady=5)

        self.extract_text_btn = ExtractTextButton(root)
        self.extract_text_btn.pack(pady=5)

        self.pdf_to_word_btn = PdfToWordButton(root)
        self.pdf_to_word_btn.pack(pady=5)

        # Progress bar
        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)

        # PDF to Sound button (pass progress bar and root window)
        self.pdf_to_sound_btn = PdfToSoundButton(root, self.progress, self.root)
        self.pdf_to_sound_btn.pack(pady=5)

        self.exit_btn = tk.Button(root, text="Exit", command=root.quit)
        self.exit_btn.pack(pady=5)