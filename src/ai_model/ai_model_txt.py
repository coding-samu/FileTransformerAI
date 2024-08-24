from ai_model.ai_model_translate import UniversalTranslator
from ai_model.ai_model_docx import DOCXPDF
from utils.utils_file import load_file_txt, save_file_txt, save_file_pdf, save_file_docx
import os
import shutil

class TXTPDF:
    def __init__(self):
        pass

    def convert(self, input_txt_path, output_pdf_path):
        try:
            # Converti il file txt in docx utilizzando la classe TXTDOCX
            txt_docx = TXTDOCX()
            # Creazione del percorso del file temporaneo docx
            output_docx_path = f'temp_file/{input_txt_path}.docx'
            # Crea le cartelle necessarie
            os.makedirs(os.path.dirname(output_docx_path), exist_ok=True)
            if txt_docx.convert(input_txt_path, output_docx_path) == 1:
                raise Exception(f"Errore durante la conversione del file {input_txt_path}")
            # Converti il file docx in pdf utilizzando la classe DOCXPDF
            docx_pdf = DOCXPDF()
            if docx_pdf.convert(output_docx_path, output_pdf_path) == 0:
                print(f"Salvataggio completato!")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file PDF: {output_pdf_path}")
        except Exception as e:
            print(f"Errore durante la conversione del file {input_txt_path}: {e}")
            return 1
        finally:
            try:
                # Elimina la cartella temporanea e tutto il suo contenuto
                shutil.rmtree('temp_file')
                print(f"Cartella temporanea eliminata: temp_file")
            except Exception as e:
                print(f"Errore durante l'eliminazione della cartella temporanea: temp_file. Dettagli: {e}")

class TXTJPG:
    pass # TODO: Implementare la conversione di file TXT in JPG

class TXTPNG:
    pass # TODO: Implementare la conversione di file TXT in PNG

class TXTDOCX:
    def __init__(self):
        pass

    def convert(self, input_txt_path, output_docx_path):
        try:
            text = load_file_txt(input_txt_path)
            if text == 1:
                raise Exception(f"Errore durante il caricamento del file TXT: {input_txt_path}")
            if save_file_docx(text, output_docx_path) == 0:
                print(f"Salvataggio completato!")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file DOCX: {output_docx_path}")
        except Exception as e:
            print(f"Errore durante la conversione del file {input_txt_path}: {e}")
            return 1

class TXTSpeech:
    pass # TODO: Implementare la conversione di file TXT in file audio

class TXTTranslate:
    def __init__(self, source_language, target_language):
        self.translator = UniversalTranslator(source_language, target_language)
    
    def convert(self, input_txt_path, output_txt_path):
        try:
            text = load_file_txt(input_txt_path)
            if text == 1:
                raise Exception(f"Errore durante il caricamento del file TXT: {input_txt_path}")
            translated_text = self.translator.convert(text)
            if save_file_txt(translated_text, output_txt_path) == 0:
                print(f"Salvataggio completato!")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file TXT: {output_txt_path}")
        except Exception as e:
            print(f"Errore durante la conversione del file {input_txt_path}: {e}")
            return 1
        
class TXTSummary:
    pass # TODO: Implementare la generazione di riassunti da file TXT

class TXTImageGen:
    pass # TODO: Implementare la generazione di immagini da file TXT

class TXTWrite:
    pass # TODO: Implementare la scrittura di testo in file TXT