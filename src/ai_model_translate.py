from translate import UniversalTranslator

def get_translate_model(source_lang, target_lang):
    try:
        return UniversalTranslator(source_lang, target_lang)
    except Exception as e:
        print(f"Non è presente un modello per la conversione da {source_lang} a {target_lang}.")
        return None