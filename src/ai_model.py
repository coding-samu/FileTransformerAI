from TextConverter import translation_en_to_fr, translation_en_to_de
from ImageConverter import better_image

def get_converter(conversion_type):
    if conversion_type == "text_en_to_fr":
        return translation_en_to_fr()
    elif conversion_type == "text_en_to_de":
        return translation_en_to_de()
    elif conversion_type == "better_image":
        return better_image()
    else:
        return None
