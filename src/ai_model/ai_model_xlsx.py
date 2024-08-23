from utils.utils_file import save_file_docx, save_file_txt, save_file_pdf

import os
import subprocess

class XLSXPDF:
    def __init__(self):
        pass

    def convert(self, input_xlsx_path, output_pdf_path):
        try:
            # Verifica che il file di input sia un file XLSX valido
            if not input_xlsx_path.endswith('.xlsx'):
                raise Exception(f"Il file {input_xlsx_path} non è un file XLSX valido.")

            # Converti XLSX a PDF usando LibreOffice
            command = [
                "libreoffice",
                "--headless",  # Run without GUI
                "--convert-to", "pdf",  # Convert to PDF
                "--outdir", os.path.dirname(output_pdf_path),  # Output directory
                input_xlsx_path
            ]
            
            subprocess.run(command, check=True)

            # Rinominare il file PDF convertito se necessario
            generated_pdf_path = os.path.join(
                os.path.dirname(output_pdf_path), 
                os.path.splitext(os.path.basename(input_xlsx_path))[0] + ".pdf"
            )
            os.rename(generated_pdf_path, output_pdf_path)
            
            print(f"Conversione completata: {output_pdf_path}")
            return 0
        
        except subprocess.CalledProcessError as e:
            print(f"Errore durante la conversione del file {input_xlsx_path}: {e}")
            return 1
        
        except Exception as e:
            print(f"Errore durante la conversione del file {input_xlsx_path}: {e}")
            return 1

class XLSXJPG:
    pass

class XLSXPNG:
    pass

class XLSXDOCX:
    pass

class XLSXTXT:
    pass

class XLSXSVG:
    pass