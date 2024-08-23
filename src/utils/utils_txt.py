from ai_model.ai_model_txt import TXTPDF, TXTJPG, TXTPNG, TXTDOCX, TXTSpeech, TXTTranslate
from utils.utils_translate import get_languages

def get_txt_model(conversion_type, input_file):
    match conversion_type:
        case "pdf":
            return txt_to_pdf(input_file)
        case "jpg":
            return txt_to_jpg(input_file)
        case "png":
            return txt_to_png(input_file)
        case "docx":
            return txt_to_docx(input_file)
        case "tts":
            return txt_to_speech(input_file)
        case "translate":
            return txt_to_translate(input_file)
        case _:
            print("Tipo di conversione non supportato.")
            return 1
        
def get_type_conversion():
    print("Come desideri convertire il file TXT? (pdf, jpg, png, docx, tts, translate): ")
    return input()

def txt(input_file):
    conversion_type = get_type_conversion()
    return get_txt_model(conversion_type, input_file)

def txt_to_pdf(input_file):
    try:
        txt_pdf = TXTPDF()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if txt_pdf.convert(f'input_files/{input_file}', f'output_files/{base_name}.pdf') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1
    
def txt_to_jpg(input_file):
    try:
        txt_jpg = TXTJPG()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if txt_jpg.convert(f'input_files/{input_file}', f'output_files/{base_name}.jpg') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1
    
def txt_to_png(input_file):
    try:
        txt_png = TXTPNG()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if txt_png.convert(f'input_files/{input_file}', f'output_files/{base_name}.png') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1
    
def txt_to_docx(input_file):
    try:
        txt_docx = TXTDOCX()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if txt_docx.convert(f'input_files/{input_file}', f'output_files/{base_name}.docx') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1
    
def txt_to_speech(input_file):
    try:
        txt_speech = TXTSpeech()
        txt_speech.convert(f'input_files/{input_file}')
        return 0
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1

def txt_to_translate(input_file):
    try:
        source_lang, target_lang = get_languages()
        txt_translate = TXTTranslate()
        txt_translate.convert(f'input_files/{input_file}', source_lang, target_lang)
        return 0
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1