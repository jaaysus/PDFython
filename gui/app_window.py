import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from core.txt_to_pdf import convert_txt_to_pdf
from core.excel_to_pdf import convert_excel_to_pdf
from core.pdf_text_extractor import extract_text_from_pdf
from core.pdf_to_word import convert_pdf_to_word
from core.pdf_to_sound import convert_pdf_to_sound  # Import the standalone function

# List of supported languages by gTTS
SUPPORTED_LANGUAGES = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "zh": "Chinese (Simplified)",
    "ja": "Japanese",
    "ru": "Russian",
    "ar": "Arabic",
    "hi": "Hindi",
    "pt": "Portuguese",
    "ko": "Korean",
    "nl": "Dutch",
    "tr": "Turkish",
    "pl": "Polish",
    "sv": "Swedish",
    "fi": "Finnish",
    "no": "Norwegian",
    "da": "Danish",
    "el": "Greek",
    "cs": "Czech",
    "th": "Thai",
    "vi": "Vietnamese",
    "id": "Indonesian",
    "ms": "Malay",
    "fil": "Filipino",
    "hu": "Hungarian",
    "ro": "Romanian",
    "uk": "Ukrainian",
    "bg": "Bulgarian",
    "hr": "Croatian",
    "sk": "Slovak",
    "sl": "Slovenian",
    "sr": "Serbian",
    "ca": "Catalan",
    "et": "Estonian",
    "lv": "Latvian",
    "lt": "Lithuanian",
    "is": "Icelandic",
    "ga": "Irish",
    "mt": "Maltese",
    "sq": "Albanian",
    "mk": "Macedonian",
    "cy": "Welsh",
    "af": "Afrikaans",
    "sw": "Swahili",
    "zu": "Zulu",
    "xh": "Xhosa",
    "st": "Southern Sotho",
    "tn": "Tswana",
    "sn": "Shona",
    "so": "Somali",
    "ha": "Hausa",
    "yo": "Yoruba",
    "ig": "Igbo",
    "mg": "Malagasy",
    "ny": "Chichewa",
    "km": "Khmer",
    "lo": "Lao",
    "my": "Burmese",
    "gl": "Galician",
    "eu": "Basque",
    "jw": "Javanese",
    "su": "Sundanese",
    "ne": "Nepali",
    "si": "Sinhala",
    "pa": "Punjabi",
    "ta": "Tamil",
    "te": "Telugu",
    "kn": "Kannada",
    "ml": "Malayalam",
    "mr": "Marathi",
    "gu": "Gujarati",
    "bn": "Bengali",
    "ur": "Urdu",
    "fa": "Persian",
    "he": "Hebrew",
    "am": "Amharic",
    "ti": "Tigrinya",
    "om": "Oromo",
    "ku": "Kurdish",
    "ps": "Pashto",
    "sd": "Sindhi",
    "bo": "Tibetan",
    "dz": "Dzongkha",
    "ka": "Georgian",
    "hy": "Armenian",
    "az": "Azerbaijani",
    "uz": "Uzbek",
    "kk": "Kazakh",
    "ky": "Kyrgyz",
    "tg": "Tajik",
    "tk": "Turkmen",
    "mn": "Mongolian",
    "ug": "Uyghur",
    "iu": "Inuktitut",
    "oj": "Ojibwe",
    "cr": "Cree",
    "kmb": "Kimbundu",
    "ln": "Lingala",
    "lg": "Ganda",
    "rw": "Kinyarwanda",
    "ak": "Akan",
    "ee": "Ewe",
    "tw": "Twi",
    "yo": "Yoruba",
    "ff": "Fulah",
    "rn": "Rundi",
    "ng": "Ndonga",
    "hz": "Herero",
    "kj": "Kuanyama",
    "sg": "Sango",
    "kg": "Kongo",
    "lu": "Luba-Katanga",
    "mg": "Malagasy",
    "ny": "Chichewa",
    "sn": "Shona",
    "st": "Southern Sotho",
    "tn": "Tswana",
    "ts": "Tsonga",
    "ve": "Venda",
    "xh": "Xhosa",
    "zu": "Zulu",
}

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
            # Create a new window for language selection
            lang_window = tk.Toplevel(self.root)
            lang_window.title("Select Language")
            lang_window.geometry("300x100")

            # Label
            tk.Label(lang_window, text="Select a language:").pack(pady=5)

            # Combobox for language selection
            lang_var = tk.StringVar()
            lang_combobox = ttk.Combobox(lang_window, textvariable=lang_var)
            lang_combobox["values"] = list(SUPPORTED_LANGUAGES.values())  # Display language names
            lang_combobox.current(0)  # Set default to English
            lang_combobox.pack(pady=5)

            # Button to confirm selection
            def confirm_language():
                selected_language_name = lang_var.get()
                # Find the language code for the selected language name
                selected_lang_code = [code for code, name in SUPPORTED_LANGUAGES.items() if name == selected_language_name][0]
                lang_window.destroy()  # Close the language selection window

                try:
                    audio_file = convert_pdf_to_sound(file_path, lang=selected_lang_code)
                    messagebox.showinfo("Success", f"Audio file saved as {audio_file}")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to convert PDF to sound: {e}")

            tk.Button(lang_window, text="Confirm", command=confirm_language).pack(pady=5)

