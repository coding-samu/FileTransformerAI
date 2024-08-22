from utils.utils_file import save_file_jpg, save_file_pdf, save_file_png, save_file_txt, save_file_xlsx

import subprocess
import os

from docx import Document

from transformers import BartTokenizer, BartForConditionalGeneration

class DOCXPDF:
    def __init__(self):
        pass

    def convert(self, input_docx_path, output_pdf_path):
        try:
            # Verifica che il file di input sia un file DOCX valido
            if not input_docx_path.endswith('.docx'):
                raise Exception(f"Il file {input_docx_path} non è un file DOCX valido.")

            # Converti DOCX a PDF usando LibreOffice
            command = [
                "libreoffice",
                "--headless",  # Run without GUI
                "--convert-to", "pdf",  # Convert to PDF
                "--outdir", os.path.dirname(output_pdf_path),  # Output directory
                input_docx_path
            ]
            
            subprocess.run(command, check=True)

            # Rinominare il file PDF convertito se necessario
            generated_pdf_path = os.path.join(
                os.path.dirname(output_pdf_path), 
                os.path.splitext(os.path.basename(input_docx_path))[0] + ".pdf"
            )
            os.rename(generated_pdf_path, output_pdf_path)
            
            print(f"Conversione completata: {output_pdf_path}")
            return 0
        
        except subprocess.CalledProcessError as e:
            print(f"Errore durante la conversione del file {input_docx_path}: {e}")
            return 1
        
        except Exception as e:
            print(f"Errore durante la conversione del file {input_docx_path}: {e}")
            return 1

class DOCXJPG:
    pass # TODO: implementare la conversione da DOCX a JPG

class DOCXPNG:
    pass # TODO: implementare la conversione da DOCX a PNG

class DOCXXLSX:
    pass # TODO: implementare la conversione da DOCX a XLSX

class DOCXTXT:
    def __init__(self):
        pass

    def convert(self, input_docx_path, output_txt_path):
        try:
            # Carica il file DOCX
            document = Document(input_docx_path)

            # Estrai il testo dal file DOCX
            full_text = []
            for paragraph in document.paragraphs:
                full_text.append(paragraph.text)

            # Combina il testo in un'unica stringa separata da nuove linee
            text = "\n".join(full_text)

            # Salva il testo estratto nel file TXT
            if save_file_txt(text, output_txt_path) == 0:
                print(f"Conversione completata: {output_txt_path}")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file TXT: {output_txt_path}")

        except Exception as e:
            print(f"Errore durante la conversione del file {input_docx_path}: {e}")
            return 1

class DOCXSVG:
    pass # TODO: implementare la conversione da DOCX a SVG

class DOCXTXTSummary:
    def __init__(self):
        # Inizializza il modello e il tokenizer per il riassunto
        self.tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
        self.model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

    def convert(self, input_docx_path, output_txt_path):
        try:
            # Carica il file DOCX
            document = Document(input_docx_path)

            # Estrai il testo dal file DOCX
            full_text = []
            for paragraph in document.paragraphs:
                full_text.append(paragraph.text)

            # Combina il testo in un'unica stringa separata da nuove linee
            text = "\n".join(full_text)

            # Preprocessa il testo per il modello
            inputs = self.tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)

            # Genera il riassunto
            summary_ids = self.model.generate(
                inputs["input_ids"],
                max_length=150,
                min_length=40,
                length_penalty=2.0,
                num_beams=4,
                early_stopping=True
            )

            # Decodifica il riassunto generato
            summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

            # Salva il riassunto nel file TXT
            if save_file_txt(summary, output_txt_path) == 0:
                print(f"Riassunto completato e salvato in: {output_txt_path}")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file TXT: {output_txt_path}")

        except Exception as e:
            print(f"Errore durante la conversione del file {input_docx_path}: {e}")
            return 1