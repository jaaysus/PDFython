import PyPDF2
from gtts import gTTS
import os

class PDFToSoundConverter:
    def __init__(self):
        self.audio_file = "output.mp3"

    def convert_pdf_to_sound(self, pdf_path):
        """Convert PDF text to an audio file."""
        try:
            # Extract text from PDF
            with open(pdf_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"

            # Convert text to speech
            tts = gTTS(text, lang="en")
            tts.save(self.audio_file)
            return self.audio_file
        except Exception as e:
            raise Exception(f"Failed to convert PDF to sound: {e}")