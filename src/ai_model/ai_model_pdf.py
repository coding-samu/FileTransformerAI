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
from utils.utils_file import save_file_jpg, save_file_png, save_file_xlsx, save_file_txt, save_file_pdf, save_file_docx
import pdfplumber
import pandas as pd
import openpyxl

class PDFOCR:
    def __init__(self):
        # Imposta il percorso dell'eseguibile Tesseract
        pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

    def perform_ocr(self, image):
        # Esegui l'OCR sull'immagine e restituisci il testo
        text = pytesseract.image_to_string(image)
        return text

    def convert(self, input_pdf_path, output_pdf_path):
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

            # Salva il PDF con il testo OCR
            if save_file_pdf(pdf_writer, output_pdf_path) == 0:
                print(f"Conversione completata: {output_pdf_path}")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file PDF {output_pdf_path}")
        except Exception as e:
            print(f"Errore durante la conversione del file {input_pdf_path}: {e}")
            return 1
        
class PDFDOCX:
    def __init__(self):
        pass

    def convert(self, input_pdf_path, output_docx_path):
        try:
            # Crea un oggetto PdfReader
            pdf_reader = PdfReader(input_pdf_path)
            extractor = PDFTextExtractor()
            text = extractor.extract_text(pdf_reader)
            if text == 1:
                raise Exception("Errore durante l'estrazione del testo dal PDF")
            # Salva il testo su disco
            if save_file_docx(text, output_docx_path) == 0:
                print(f"Conversione completata: {output_docx_path}")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file DOCX {output_docx_path}")
        except Exception as e:
            print(f"Errore durante la conversione del file {input_pdf_path}: {e}")
            return 1

class PDFJPG:
    def __init__(self):
        pass

    def convert(self, input_pdf_path, output_jpg_path, page_number=1, quality=95):
        try:
            input_pdf = PdfReader(input_pdf_path)
            if page_number < 1 or page_number > len(input_pdf.pages):
                raise ValueError(f"Numero di pagina non valido: {page_number}")
            # Converte la pagina specificata del PDF in un'immagine PIL
            images = convert_from_path(input_pdf_path, first_page=page_number, last_page=page_number)
            if images:
                # Salva l'immagine in un buffer temporaneo come JPG
                img_byte_arr = io.BytesIO()
                images[0].save(img_byte_arr, format='JPEG', quality=quality)

                # Salva l'immagine su disco
                if save_file_jpg(img_byte_arr.getvalue(), output_jpg_path) == 0:
                    print(f"Conversione completata: {output_jpg_path}")
                    return 0
                else:
                    raise Exception(f"Errore durante il salvataggio dell'immagine {output_jpg_path}")
            else:
                raise Exception(f"Errore durante la conversione della pagina {page_number} del file {input_pdf_path}")
        except Exception as e:
            print(f"Errore durante la conversione del file {input_pdf_path}: {e}")
            return 1

class PDFPNG:
    def __init__(self):
        pass

    def convert(self, input_pdf_path, output_png_path, page_number=1, quality=95):
        try:
            input_pdf = PdfReader(input_pdf_path)
            if page_number < 1 or page_number > len(input_pdf.pages):
                raise ValueError(f"Numero di pagina non valido: {page_number}")
            # Converte la pagina specificata del PDF in un'immagine PIL
            images = convert_from_path(input_pdf_path, first_page=page_number, last_page=page_number)
            if images:
                # Salva l'immagine in un buffer temporaneo come PNG
                img_byte_arr = io.BytesIO()
                images[0].save(img_byte_arr, format='PNG', quality=quality)

                # Salva l'immagine su disco
                if save_file_png(img_byte_arr.getvalue(), output_png_path) == 0:
                    print(f"Conversione completata: {output_png_path}")
                    return 0
                else:
                    raise Exception(f"Errore durante il salvataggio dell'immagine {output_png_path}")
            else:
                raise Exception(f"Errore durante la conversione della pagina {page_number} del file {input_pdf_path}")
        except Exception as e:
            print(f"Errore durante la conversione del file {input_pdf_path}: {e}")
            return 1

class PDFXLSX:
    def __init__(self):
        pass

    def convert(self, input_pdf_path, output_xlsx_path, page_number=1):
        try:
            # Apertura del file PDF con pdfplumber
            with pdfplumber.open(input_pdf_path) as pdf:
                if page_number < 1 or page_number > len(pdf.pages):
                    raise ValueError(f"Numero di pagina non valido: {page_number}")

                # Estrai la pagina specificata
                page = pdf.pages[page_number - 1]

                # Cerca tabelle nella pagina
                tables = page.extract_tables()

                if not tables:
                    raise Exception(f"Nessuna tabella trovata nella pagina {page_number} del file {input_pdf_path}")

                # Converti la prima tabella in un DataFrame pandas
                data = pd.DataFrame(tables[0])

                # Converte i dati in un elenco di elenchi, adatto a openpyxl
                data_list = data.values.tolist()

                # Salva i dati come file XLSX
                if save_file_xlsx(data_list, output_xlsx_path) == 0:
                    print(f"Conversione completata: {output_xlsx_path}")
                    return 0
                else:
                    raise Exception(f"Errore durante il salvataggio del file XLSX {output_xlsx_path}")
        except Exception as e:
            print(f"Errore durante la conversione del file {input_pdf_path}: {e}")
            return 1

class PDFTXT:
    def __init__(self):
        pass

    def convert(self, input_pdf_path, output_txt_path):
        try:
            # Crea un oggetto PdfReader
            pdf_reader = PdfReader(input_pdf_path)
            extractor = PDFTextExtractor()
            text = extractor.extract_text(pdf_reader)
            if text == 1:
                raise Exception("Errore durante l'estrazione del testo dal PDF")

            # Salva il testo su disco
            if save_file_txt(text, output_txt_path) == 0:
                print(f"Conversione completata: {output_txt_path}")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file TXT {output_txt_path}")
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

    def summarize(self, input_pdf_path, output_txt_path):
        try:
            # Estrai il testo dal PDF
            pdf_reader = PdfReader(input_pdf_path)
            extractor = PDFTextExtractor()
            text = extractor.extract_text(pdf_reader)
            if text == 1:
                raise Exception("Errore durante l'estrazione del testo dal PDF")
            summary = self.summarizer(text)
            # Salva il riassunto su disco
            if save_file_txt(summary[0]['summary_text'], output_txt_path) == 0:
                print(f"Conversione completata: {output_txt_path}")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file TXT {output_txt_path}") 
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