from traduzione_en_to_fr import TextConverter
from better_image import ImageConverter

def get_converter(conversion_type):
    if conversion_type == "text_en_to_fr":
        return TextConverter()
    elif conversion_type == "better_image":
        return ImageConverter()
    else:
        return None
