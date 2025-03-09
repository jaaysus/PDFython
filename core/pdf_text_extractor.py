import pdfplumber

def extract_text_from_pdf(file_path, save_path):
    try:
        extracted_text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                extracted_text += page.extract_text() + "\n"

        with open(save_path, "w", encoding="utf-8") as file:
            file.write(extracted_text)

    except Exception as e:
        raise Exception(f"Failed to extract text: {e}")
