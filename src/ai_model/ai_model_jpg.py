from utils.utils_file import save_file_pdf, save_file_png, save_file_txt
from utils.utils_file import load_file_jpg

from PIL import Image
import io
import pytesseract
from PyPDF2 import PdfWriter, PdfReader

import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

class JPGPDF:
    def __init__(self):
        pass

    def convert(self, input_jpg_path, output_pdf_path):
        try:
            # Carica il file JPG utilizzando la funzione load_file_jpg
            img_data = load_file_jpg(input_jpg_path)
            if img_data is None:
                raise Exception(f"Errore nel caricamento del file JPG: {input_jpg_path}")

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
            print(f"Errore durante la conversione del file {input_jpg_path}: {e}")
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

class JPGPNG:
    def __init__(self):
        pass

    def convert(self, input_jpg_path, output_png_path):
        try:
            # Carica il file JPG utilizzando la funzione load_file_jpg
            img_data = load_file_jpg(input_jpg_path)
            if img_data is None:
                raise Exception(f"Errore nel caricamento del file JPG: {input_jpg_path}")

            # Crea un oggetto BytesIO dai dati dell'immagine
            img_byte_arr = io.BytesIO(img_data)

            # Converte l'immagine in un oggetto PIL
            image = Image.open(img_byte_arr)

            # Salva l'immagine come PNG utilizzando la funzione save_file_png
            png_bytes = self.image_to_png_bytes(image)
            if save_file_png(png_bytes, output_png_path) == 0:
                print(f"Conversione completata: {output_png_path}")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file PNG: {output_png_path}")

        except Exception as e:
            print(f"Errore durante la conversione del file {input_jpg_path}: {e}")
            return 1

    def image_to_png_bytes(self, image):
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        return img_byte_arr.getvalue()

class JPGTXT:
    def __init__(self):
        pass

    def convert(self, input_jpg_path, output_txt_path):
        try:
            # Carica il file JPG utilizzando la funzione load_file_jpg
            img_data = load_file_jpg(input_jpg_path)
            if img_data is None:
                raise Exception(f"Errore nel caricamento del file JPG: {input_jpg_path}")

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
            print(f"Errore durante la conversione del file {input_jpg_path}: {e}")
            return 1
        
class JPGAltText:
    def __init__(self):
        # Inizializza il processore e il modello BLIP per la generazione di descrizioni testuali
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    def convert(self, input_jpg_path, output_txt_path):
        try:
            # Carica l'immagine
            image = Image.open(input_jpg_path).convert("RGB")

            # Preprocessa l'immagine e preparala per il modello
            inputs = self.processor(image, return_tensors="pt")

            # Genera la didascalia (alt text) per l'immagine
            caption_ids = self.model.generate(**inputs)
            caption = self.processor.decode(caption_ids[0], skip_special_tokens=True)

            # Salva la didascalia nel file di output
            if save_file_txt(caption, output_txt_path) == 0:
                print(f"Alt text generato e salvato in: {output_txt_path}")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file TXT: {output_txt_path}")

        except Exception as e:
            print(f"Errore durante la conversione del file {input_jpg_path}: {e}")
            return 1