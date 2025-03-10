import os
import PyPDF2
from gtts import gTTS

class PDFToSoundConverter:
    def __init__(self):
        pass

    def convert_pdf_to_sound(self, pdf_path):
        """Convert PDF text to an audio file with the original file name in the same directory."""
        try:
            # Extract text from PDF
            with open(pdf_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"

            # Get the directory and original file name (without extension)
            directory = os.path.dirname(pdf_path)
            file_name = os.path.splitext(os.path.basename(pdf_path))[0]
            audio_file = os.path.join(directory, f"{file_name}.mp3")

            # Convert text to speech
            tts = gTTS(text, lang="en")
            tts.save(audio_file)
            return audio_file
        except Exception as e:
            raise Exception(f"Failed to convert PDF to sound: {e}")
