from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import chardet

def convert_txt_to_pdf(file_path, save_path):
    try:
        with open(file_path, "rb") as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)  
            encoding = result["encoding"]

        with open(file_path, "r", encoding=encoding, errors="replace") as file:
            content = file.read()

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

    except Exception as e:
        raise Exception(f"Failed to convert TXT: {e}")
