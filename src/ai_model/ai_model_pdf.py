import pytesseract
from transformers import pipeline
from pdf2image import convert_from_path
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfWriter, PdfReader
import io
import os
import tempfile
from PIL import Image
import subprocess

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
    def __init__(self):
        pass

    def convert(self, input_pdf_path):
        try:
            # Crea un oggetto PdfReader
            pdf_reader = PdfReader(input_pdf_path)
            extractor = PDFTextExtractor()
            return extractor.extract_text(pdf_reader)
        except Exception as e:
            print(f"Errore durante la conversione del file {input_pdf_path}: {e}")
            return None

class PDFJPG:
    pass #TODO: implementare la conversione da PDF a JPG

class PDFPNG:
    pass #TODO: implementare la conversione da PDF a PNG

class PDFXLSX:
    pass #TODO: implementare la conversione da PDF a XLSX

class PDFTXT:
    def __init__(self):
        pass

    def convert(self, input_pdf_path):
        try:
            # Crea un oggetto PdfReader
            pdf_reader = PdfReader(input_pdf_path)
            extractor = PDFTextExtractor()
            return extractor.extract_text(pdf_reader)
        except Exception as e:
            print(f"Errore durante la conversione del file {input_pdf_path}: {e}")
            return 1

class PDFSVG:
    def __init__(self):
        pass

    def convert_to_svg(self, input_pdf_path, output_svg_path, page_number=1):
        try:
            pdf = PdfReader(input_pdf_path)
            if page_number < 1 or page_number > len(pdf.pages):
                raise ValueError(f"Numero di pagina non valido: {page_number}")
            command = f"pdf2svg {input_pdf_path} {output_svg_path} {page_number}"
            os.system(command)
            print(f"Conversione completata: {output_svg_path}")
            return 0
        except Exception as e:
            print(f"Errore durante la conversione del file {input_pdf_path}: {e}")
            return 1

class PDFCOMPRESS:
    def __init__(self):
        pass

    def compress(self, input_pdf_path, output_pdf_path):
        try:
            subprocess.call([
                'gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                '-dPDFSETTINGS=/screen', '-dNOPAUSE', '-dQUIET', '-dBATCH',
                f'-sOutputFile={output_pdf_path}', input_pdf_path
            ])
            return 0
        except Exception as e:
            print(f"Errore durante la compressione del file {input_pdf_path}: {e}")
            return 1

class PDFTXTSUMMARY:
    def __init__(self):
        # Inizializza il modello di riassunto usando Hugging Face's pipeline
        self.summarizer = pipeline("summarization")

    def summarize(self, input_pdf_path):
        try:
            # Estrai il testo dal PDF
            pdf_reader = PdfReader(input_pdf_path)
            extractor = PDFTextExtractor()
            text = extractor.extract_text(pdf_reader)
            if text == 1:
                raise Exception("Errore durante l'estrazione del testo dal PDF")
            summary = self.summarizer(text)
            return summary[0]['summary_text']
        except Exception as e:
            print(f"Errore durante la generazione del riassunto del file {input_pdf_path}: {e}")
            return 1

class PDFTextExtractor:
    def __init__(self):
        pass

    def extract_text(self, pdf_reader):
        try:
            extracted_text = ""

            # Itera attraverso tutte le pagine del PDF
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                extracted_text += page.extract_text() + "\n"

            return extracted_text
        except Exception as e:
            print(f"Errore durante l'estrazione del testo dal PDF: {e}")
            return 1