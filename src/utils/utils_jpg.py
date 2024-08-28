from ai_model.ai_model_jpg import JPGPDF, JPGPNG, JPGTXT

import os

def get_jpg_model(conversion_type, input_file):
    match conversion_type:
        case "pdf":
            return jpg_to_pdf(input_file)
        case "png":
            return jpg_to_png(input_file)
        case "txt":
            return jpg_to_txt(input_file)
        case "alttext":
            print("Conversione alttext non ancora supportata.")
            return 1
        case _:
            print("Tipo di conversione non supportato.")
            return 1
        
def get_type_conversion():
    print("Come desideri convertire il file JPG? (pdf, png, txt, alttext): ")
    return input()

def jpg_to_pdf(input_file):
    try:
        jpg_pdf = JPGPDF()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if jpg_pdf.convert(f'input_files/{input_file}', f'output_files/{base_name}.pdf') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1
    
def jpg_to_png(input_file):
    try:
        jpg_png = JPGPNG()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if jpg_png.convert(f'input_files/{input_file}', f'output_files/{base_name}.png') == 0:
            print(f"Salvataggio completato!")
        else:
            raise Exception("Errore durante la conversione del file")
        return 0
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1

def jpg_to_txt(input_file):
    try:
        jpg_txt = JPGTXT()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if jpg_txt.convert(f'input_files/{input_file}', f'output_files/{base_name}.txt') == 0:
            print(f"Salvataggio completato!")
        else:
            raise Exception("Errore durante la conversione del file")
        return 0
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1
    
def jpg(input_file):
    conversion_type = get_type_conversion()
    return get_jpg_model(conversion_type, input_file)