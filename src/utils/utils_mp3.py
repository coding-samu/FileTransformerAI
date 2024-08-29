from ai_model.ai_model_mp3 import MP3STT
import os

def get_mp3_model(conversion_type, input_file):
    match conversion_type:
        case "stt":
            return mp3_to_stt(input_file)
        case _:
            print("Tipo di conversione non supportato.")
            return None
        
def choose_lang():
    print("Seleziona la lingua: (lingue supportate: en, it, es, fr, de)")
    lang = input()
    return lang

def get_type_conversion():
    print("Come desideri convertire il file MP3? (stt): ")
    return input()

def mp3(input_file):
    conversion_type = get_type_conversion()
    return get_mp3_model(conversion_type, input_file)

def mp3_to_stt(input_file):
    try:
        lang = choose_lang()
        mp3_stt = MP3STT(lang)
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if mp3_stt.convert(f'input_files/{input_file}', f'output_files/{base_name}.txt') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1