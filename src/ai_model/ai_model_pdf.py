import pytesseract
from pdf2image import convert_from_path
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader
import io
import os
import tempfile
from PIL import Image

class PDFOCR:
    def __init__(self):
        # Imposta il percorso dell'eseguibile Tesseract
        pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

    def perform_ocr(self, image):
        # Esegui l'OCR sull'immagine e restituisci il testo
        text = pytesseract.image_to_string(image)
        return text

    def convert(self, input_pdf_path):
        try:
            # Estrai le immagini da ciascuna pagina del PDF
            images = convert_from_path(input_pdf_path)

            # Crea un oggetto PdfWriter
            pdf_writer = PdfWriter()

            for i, image in enumerate(images):
                # Esegui OCR sulla pagina corrente
                ocr_text = self.perform_ocr(image)

                # Crea una pagina PDF con il solo testo OCR
                packet = io.BytesIO()
                can = canvas.Canvas(packet, pagesize=letter)

                # Aggiungi il testo OCR al PDF
                can.setFont("Helvetica", 10)
                text_lines = ocr_text.split('\n')
                y = letter[1] - 20  # Partiamo dal bordo superiore della pagina

                for line in text_lines:
                    can.drawString(10, y, line)
                    y -= 12  # Spostiamo verso il basso per la prossima riga

                can.save()

                # Sposta il puntatore all'inizio del buffer
                packet.seek(0)

                # Aggiungi il contenuto generato al PdfWriter
                new_pdf = PdfReader(packet)
                pdf_writer.add_page(new_pdf.pages[0])

            return pdf_writer

        except Exception as e:
            print(f"Errore durante la conversione del file {input_pdf_path}: {e}")
            return None
        
class PDFDOCX:
    pass #TODO: implementare la conversione da PDF a DOCX

class PDFJPG:
    pass #TODO: implementare la conversione da PDF a JPG

class PDFPNG:
    pass #TODO: implementare la conversione da PDF a PNG

class PDFXLSX:
    pass #TODO: implementare la conversione da PDF a XLSX

class PDFTXT:
    pass #TODO: implementare la conversione da PDF a TXT

class PDFSVG:
    pass #TODO: implementare la conversione da PDF a SVG

class PDFCOMPRESS:
    pass #TODO: implementare la compressione di un PDF

class PDFTXTSUMMARY:
    pass #TODO: implementare la generazione di un riassunto di un PDF