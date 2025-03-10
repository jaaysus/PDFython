import os
import time
import threading
import PyPDF2
from gtts import gTTS

def convert_pdf_to_sound(pdf_path, lang="en", progress_callback=None):
    """Convert PDF text to an audio file with real-time progress updates."""
    try:
        # Phase 1: Extract text from the PDF (25% of the progress)
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""

            # Extract all text from the PDF
            for page in reader.pages:
                text += page.extract_text() + "\n"

            # Update progress to 25% after text extraction
            if progress_callback:
                progress_callback(25)

        # Phase 2: Convert text to speech (75% of the progress)
        def run_tts_conversion():
            """Run the gTTS conversion in a separate thread."""
            try:
                # Get the directory and original file name (without extension)
                directory = os.path.dirname(pdf_path)
                file_name = os.path.splitext(os.path.basename(pdf_path))[0]
                audio_file = os.path.join(directory, f"{file_name}.mp3")

                # Convert text to speech
                tts = gTTS(text, lang=lang)
                tts.save(audio_file)
            except Exception as e:
                if progress_callback:
                    progress_callback(-1)  # Indicate error
                raise e

        # Start the gTTS conversion in a separate thread
        tts_thread = threading.Thread(target=run_tts_conversion)
        tts_thread.start()

        # Record the start time for progress simulation
        start_time = time.time()
        estimated_conversion_time = 10  # Adjust based on your observations

        # Simulate progress updates while the conversion is running
        while tts_thread.is_alive():
            if progress_callback:
                # Increment progress from 25% to 80% while the thread is running
                elapsed_time = time.time() - start_time
                current_progress = 25 + (elapsed_time / estimated_conversion_time * 75)
                progress_callback(min(current_progress, 80))  # Cap at 80% until done
            time.sleep(3)  # Update progress every 0.1 seconds

        # Wait for the thread to finish
        tts_thread.join()

        # Update progress to 100% after the thread is done
        if progress_callback:
            progress_callback(100)

    except Exception as e:
        raise Exception(f"Failed to convert PDF to sound: {e}")