from ai_model.ai_model_translate import UniversalTranslator
from utils.utils_file import load_file_txt, save_file_txt
class TXTPDF:
    pass

class TXTJPG:
    pass

class TXTPNG:
    pass

class TXTDOCX:
    pass

class TXTSpeech:
    pass

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
    pass

class TXTImageGen:
    pass

class TXTWrite:
    pass