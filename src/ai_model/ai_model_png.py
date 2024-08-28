from utils.utils_file import save_file_pdf, save_file_jpg, save_file_txt, load_file_png

from PIL import Image
import io
import pytesseract
from PyPDF2 import PdfWriter, PdfReader

class PNGPDF:
    def __init__(self):
        pass

    def convert(self, input_png_path, output_pdf_path):
        try:
            # Carica il file PNG utilizzando la funzione load_file_png
            img_data = load_file_png(input_png_path)
            if img_data is None:
                raise Exception(f"Errore nel caricamento del file PNG: {input_png_path}")

            # Crea un oggetto BytesIO dai dati dell'immagine
            img_byte_arr = io.BytesIO(img_data)

            # Converte l'immagine in un oggetto PIL
            image = Image.open(img_byte_arr)

            # Converti in RGB se l'immagine è in un altro formato (es. PNG con trasparenza)
            if image.mode in ("RGBA", "LA"):
                image = image.convert("RGB")

            # Converti l'immagine in un PDF
            pdf_writer = self.image_to_pdf_writer(image)

            # Salva il PDF utilizzando la funzione save_file_pdf
            if save_file_pdf(pdf_writer, output_pdf_path) == 0:
                print(f"Conversione completata: {output_pdf_path}")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file PDF: {output_pdf_path}")

        except Exception as e:
            print(f"Errore durante la conversione del file {input_png_path}: {e}")
            return 1

    def image_to_pdf_writer(self, image):
        # Crea un oggetto PdfWriter
        pdf_writer = PdfWriter()

        # Converti l'immagine in bytes e aggiungila al writer
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PDF')

        # Aggiungi il PDF generato al PdfWriter
        pdf_writer.add_page(PdfReader(io.BytesIO(img_byte_arr.getvalue())).pages[0])

        return pdf_writer
    
class PNGJPG:
    def __init__(self):
        pass

    def convert(self, input_png_path, output_jpg_path):
        try:
            # Carica il file PNG utilizzando la funzione load_file_png
            img_data = load_file_png(input_png_path)
            if img_data is None:
                raise Exception(f"Errore nel caricamento del file PNG: {input_png_path}")

            # Crea un oggetto BytesIO dai dati dell'immagine
            img_byte_arr = io.BytesIO(img_data)

            # Converte l'immagine in un oggetto PIL
            image = Image.open(img_byte_arr)

            # Converti in RGB se l'immagine è in un altro formato (es. P, LA)
            if image.mode != "RGB":
                image = image.convert("RGB")

            # Salva l'immagine come JPG utilizzando la funzione save_file_jpg
            jpg_bytes = self.image_to_jpg_bytes(image)
            if save_file_jpg(jpg_bytes, output_jpg_path) == 0:
                print(f"Conversione completata: {output_jpg_path}")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file JPG: {output_jpg_path}")

        except Exception as e:
            print(f"Errore durante la conversione del file {input_png_path}: {e}")
            return 1

    def image_to_jpg_bytes(self, image):
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='JPEG')
        return img_byte_arr.getvalue()
    
class PNGTXT:
    def __init__(self):
        pass

    def convert(self, input_png_path, output_txt_path):
        try:
            # Carica il file PNG utilizzando la funzione load_file_png
            img_data = load_file_png(input_png_path)
            if img_data is None:
                raise Exception(f"Errore nel caricamento del file PNG: {input_png_path}")

            # Crea un oggetto BytesIO dai dati dell'immagine
            img_byte_arr = io.BytesIO(img_data)

            # Converte l'immagine in un oggetto PIL
            image = Image.open(img_byte_arr)

            # Usa Tesseract per estrarre il testo dall'immagine
            extracted_text = pytesseract.image_to_string(image)

            # Salva il testo estratto utilizzando la funzione save_file_txt
            if save_file_txt(extracted_text, output_txt_path) == 0:
                print(f"Testo estratto e salvato in: {output_txt_path}")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file TXT: {output_txt_path}")

        except Exception as e:
            print(f"Errore durante la conversione del file {input_png_path}: {e}")
            return 1
        
class PNGAltText:
    def __init__(self):
        pass

    def convert(self, input_png_path):
        try:
            # Carica il file PNG utilizzando la funzione load_file_png
            img_data = load_file_png(input_png_path)
            if img_data is None:
                raise Exception(f"Errore nel caricamento del file PNG: {input_png_path}")

            # TODO: Implementare l'estrazione dell'alt text dall'immagine

            return 0

        except Exception as e:
            print(f"Errore durante la conversione del file {input_png_path}: {e}")
            return None