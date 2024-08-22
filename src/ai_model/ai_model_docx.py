from utils.utils_file import save_file_jpg, save_file_pdf, save_file_png, save_file_txt, save_file_xlsx

import subprocess
import os

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
    pass # TODO: implementare la conversione da DOCX a TXT

class DOCXSVG:
    pass # TODO: implementare la conversione da DOCX a SVG

class DOCXTXTSummary:
    pass # TODO: implementare la conversione da DOCX a TXT con riassunto