from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import chardet

def convert_txt_to_pdf(file_path, save_path):
    try:
        # Detect the encoding of the input file
        with open(file_path, "rb") as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)  
            encoding = result["encoding"]

        # Read the content of the file with detected encoding
        with open(file_path, "r", encoding=encoding, errors="replace") as file:
            content = file.read()

        c = canvas.Canvas(save_path, pagesize=letter)
        c.setFont("Helvetica", 12)

        # Page dimensions (for letter size)
        width, height = letter
        margin_left = 72
        margin_bottom = 72
        margin_top = 72  # Defined margin for the top
        line_height = 14

        # Position for starting text
        y_position = height - margin_top

        # Function to manually wrap text based on page width
        def wrap_text(text, max_width):
            lines = []
            words = text.split(' ')
            current_line = ''

            for word in words:
                test_line = current_line + ' ' + word if current_line else word
                if c.stringWidth(test_line, "Helvetica", 12) <= max_width:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = word

            if current_line:
                lines.append(current_line)

            return lines

        # Write the content line by line and handle page breaks
        for line in content.splitlines():
            wrapped_lines = wrap_text(line, width - 2 * margin_left)

            for wrapped_line in wrapped_lines:
                if y_position < margin_bottom + line_height:
                    c.showPage()
                    c.setFont("Helvetica", 12)
                    y_position = height - margin_top

                c.drawString(margin_left, y_position, wrapped_line)
                y_position -= line_height

        c.save()

    except Exception as e:
        raise Exception(f"Failed to convert TXT to PDF: {e}")
