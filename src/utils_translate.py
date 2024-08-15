from utils_file import load_file_txt, save_file_txt
from ai_model_translate import UniversalTranslator

def get_translate_model(source_lang, target_lang):
    try:
        return UniversalTranslator(source_lang, target_lang)
    except Exception as e:
        print(f"Non è presente un modello per la conversione da {source_lang} a {target_lang}.")
        return None

def get_languages():
    print("Inserisci la lingua di partenza: ")
    source_lang = input()
    print("Inserisci la lingua di destinazione: ")
    target_lang = input()
    return (source_lang, target_lang)

def translate(input_file):
    t = get_languages()
    input_data = load_file_txt(f'input_files/{input_file}')
    converter = get_translate_model(t[0], t[1])
    output_data = converter.convert(input_data)
    save_file_txt(output_data, f'output_files/({t[0]}_to_{t[1]})_{input_file}')
    print(f"Salvataggio completato!")