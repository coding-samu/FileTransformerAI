import torch
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from pdf2image import convert_from_path
from PIL import Image
import io
from PyPDF2 import PdfWriter, PdfReader

class PDFOCR:
    def __init__(self):
        # Inizializza il processore e il modello TrOCR
        self.processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
        self.model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')

    def process_page(self, image):
        # Converte l'immagine in input in formato adatto al modello TrOCR
        pixel_values = self.processor(images=image, return_tensors="pt").pixel_values
        
        # Genera il testo utilizzando il modello
        generated_ids = self.model.generate(pixel_values)
        generated_text = self.processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return generated_text

    def convert(self, input_pdf_path, output_pdf_path):
        # Estrae le immagini da ciascuna pagina del PDF
        images = convert_from_path(input_pdf_path)

        # Crea un nuovo PDF con il testo OCR
        pdf_writer = PdfWriter()

        for i, image in enumerate(images):
            # Esegue OCR sulla pagina corrente
            ocr_text = self.process_page(image)
            
            # Salva la pagina originale in un buffer
            img_buffer = io.BytesIO()
            image.save(img_buffer, format="JPEG")
            img_buffer.seek(0)
            img_pdf = PdfReader(io.BytesIO(img_buffer.getvalue())).pages[0]

            # Aggiungi il testo OCR come metadati della pagina
            img_pdf.add_text(ocr_text)
            pdf_writer.add_page(img_pdf)
        
        return pdf_writer