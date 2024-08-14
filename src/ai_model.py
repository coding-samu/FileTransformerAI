from TextConverter import UniversalTranslator
from ImageConverter import better_image

def get_converter(conversion_type):
    if conversion_type == "text_en_to_fr":
        return UniversalTranslator("en", "fr")
    elif conversion_type == "text_en_to_de":
        return UniversalTranslator("en", "de")
    elif conversion_type == "text_it_to_en":
        return UniversalTranslator("it", "en")
    elif conversion_type == "better_image":
        return better_image()
    else:
        return None
