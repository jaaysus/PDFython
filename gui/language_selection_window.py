import tkinter as tk
from tkinter import ttk, messagebox
from core.pdf_to_sound import convert_pdf_to_sound
from core.languages import SUPPORTED_LANGUAGES

class LanguageSelectionWindow:
    def __init__(self, master, file_path, progress, root):
        self.master = master
        self.file_path = file_path
        self.progress = progress  # Pass the progress bar
        self.root = root  # Pass the root window

    def open_window(self):
        lang_window = tk.Toplevel(self.master)
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
            selected_lang_code = [code for code, name in SUPPORTED_LANGUAGES.items() if name == selected_language_name][0]
            lang_window.destroy()

            # Reset progress bar
            self.progress["value"] = 0
            self.root.update_idletasks()

            # Function to update the progress bar
            def update_progress(percent):
                self.progress["value"] = percent
                self.root.update_idletasks()

            try:
                # Convert PDF to sound with progress updates
                audio_file = convert_pdf_to_sound(self.file_path, lang=selected_lang_code, progress_callback=update_progress)
                messagebox.showinfo("Success", f"Audio file saved as {audio_file}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to convert PDF to sound: {e}")

        tk.Button(lang_window, text="Confirm", command=confirm_language).pack(pady=5)