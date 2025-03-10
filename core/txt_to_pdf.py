from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from pathlib import Path
import chardet
import os
import re

def convert_txt_to_pdf(file_path, save_path):
    try:
        
        with open(file_path, "rb") as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)
            encoding = result["encoding"]

        
        with open(file_path, "r", encoding=encoding, errors="replace") as file:
            content = file.read()

        c = canvas.Canvas(save_path, pagesize=letter)

        
        font_paths = {
            "latin": Path(__file__).resolve().parent.parent / 'assets' / 'fonts' / 'Arial.ttf',
            "chinese": Path(__file__).resolve().parent.parent / 'assets' / 'fonts' / 'Microsoft_YaHei_Bold.ttf',
            "korean": Path(__file__).resolve().parent.parent / 'assets' / 'fonts' / 'MalgunGothic.ttf',
            "russian": Path(__file__).resolve().parent.parent / 'assets' / 'fonts' / 'FreeSerif.ttf'
        }

        
        for font_name, font_path in font_paths.items():
            if os.path.exists(font_path):
                pdfmetrics.registerFont(TTFont(font_name, font_path))

        
        def detect_font(text):
            if re.search('[\u4e00-\u9fff]', text):  
                return "chinese"
            elif re.search('[\uac00-\ud7af]', text):  
                return "korean"
            elif re.search('[\u0400-\u04FF]', text):  
                return "russian"
            else:  
                return "latin"

        
        width, height = letter
        margin_left = 72
        margin_bottom = 72
        margin_top = 72  
        line_height = 14

        
        y_position = height - margin_top

        
        def wrap_text(text, max_width, font_name):
            lines = []
            words = text.split(' ')
            current_line = ''

            for word in words:
                test_line = current_line + ' ' + word if current_line else word
                if c.stringWidth(test_line, font_name, 12) <= max_width:
                    current_line = test_line
                else:
                    lines.append(current_line)
                    current_line = word

            if current_line:
                lines.append(current_line)

            return lines

        
        for line in content.splitlines():
            font_name = detect_font(line)  
            c.setFont(font_name, 12)
            wrapped_lines = wrap_text(line, width - 2 * margin_left, font_name)

            for wrapped_line in wrapped_lines:
                if y_position < margin_bottom + line_height:
                    c.showPage()
                    c.setFont(font_name, 12)
                    y_position = height - margin_top

                c.drawString(margin_left, y_position, wrapped_line)
                y_position -= line_height

        
        c.save()

    except Exception as e:
        raise Exception(f"Failed to convert TXT to PDF: {e}")
