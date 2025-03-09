import openpyxl
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def convert_excel_to_pdf(file_path, save_path):
    try:
        wb = openpyxl.load_workbook(file_path)
        ws = wb.active

        c = canvas.Canvas(save_path, pagesize=letter)
        c.setFont("Helvetica", 12)

        y_position = 750
        for row in ws.iter_rows(values_only=True):
            line = " | ".join(str(cell) for cell in row)
            c.drawString(72, y_position, line)
            y_position -= 14

            if y_position < 72:
                c.showPage()
                c.setFont("Helvetica", 12)
                y_position = 750

        c.save()

    except Exception as e:
        raise Exception(f"Failed to convert Excel: {e}")
