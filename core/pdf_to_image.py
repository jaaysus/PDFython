import fitz  # PyMuPDF
import os

def convert_pdf_to_images(pdf_path, output_folder, dpi=300):
    try:
        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Open the PDF
        pdf_document = fitz.open(pdf_path)

        # Loop through each page in the PDF
        image_paths = []
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)

            # Get a pixmap (image) of the page at the given DPI
            pix = page.get_pixmap(dpi=dpi)

            # Define the image path
            image_path = os.path.join(output_folder, f"page_{page_num + 1}.png")

            # Save the image
            pix.save(image_path)
            image_paths.append(image_path)

        return image_paths

    except Exception as e:
        raise Exception(f"Failed to convert PDF to images: {e}")
