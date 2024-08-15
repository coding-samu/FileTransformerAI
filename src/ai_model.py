from translate import UniversalTranslator

def get_converter(conversion_type):
    match conversion_type:
        case "text_en_to_fr":
            return UniversalTranslator("en", "fr")
        case "text_en_to_de":
            return UniversalTranslator("en", "de")
        case "text_it_to_en":
            return UniversalTranslator("it", "en")
        case _:
            return None