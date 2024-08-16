from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from pdf2image import convert_from_path
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader
import io
from PIL import Image

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

        # Crea un buffer PDF per il salvataggio temporaneo delle immagini con il testo OCR
        pdf_writer = PdfWriter()

        for i, image in enumerate(images):
            # Esegue OCR sulla pagina corrente
            ocr_text = self.process_page(image)

            # Crea una pagina PDF con l'immagine e il testo OCR
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=letter)
            
            # Aggiunge l'immagine della pagina
            img_buffer = io.BytesIO()
            image.save(img_buffer, format="JPEG")
            img_buffer.seek(0)
            can.drawImage(img_buffer, 0, 0, width=letter[0], height=letter[1])
            
            # Aggiunge il testo OCR
            can.setFont("Helvetica", 10)
            can.drawString(10, 10, ocr_text)
            can.save()

            # Unisce l'immagine con il testo OCR al PDF originale
            packet.seek(0)
            new_pdf = PdfReader(packet)
            pdf_writer.add_page(new_pdf.pages[0])

        return pdf_writer