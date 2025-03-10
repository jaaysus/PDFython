import PyPDF2
import pyttsx3

def convert_pdf_to_sound(pdf_path):
    try:
        # Extract text from PDF
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()

        # Convert text to speech
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        raise Exception(f"Failed to convert PDF to sound: {e}")