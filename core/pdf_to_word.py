from pdf2docx import Converter

def convert_pdf_to_word(pdf_path, word_path):
    try:
        cv = Converter(pdf_path)
        cv.convert(word_path, start=0, end=None)
        cv.close()
    except Exception as e:
        raise Exception(f"Failed to convert PDF to Word: {e}")