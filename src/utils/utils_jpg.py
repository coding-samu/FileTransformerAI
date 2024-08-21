from ai_model.ai_model_jpg import JPGPDF, JPGPNG, JPGTXT

def get_jpg_model(conversion_type, input_file):
    match conversion_type:
        case "pdf":
            return jpg_to_pdf(input_file)
        case "png":
            return jpg_to_png(input_file)
        case "txt":
            return jpg_to_txt(input_file)
        case _:
            print("Tipo di conversione non supportato.")
            return 1
        
def get_type_conversion():
    print("Come desideri convertire il file JPG? (pdf, png, txt): ")
    return input()

def jpg_to_pdf(input_file):
    try:
        jpg_pdf = JPGPDF()
        if jpg_pdf.convert(f'input_files/{input_file}', f'output_files/{input_file}.pdf') == 0:
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
        if jpg_png.convert(f'input_files/{input_file}', f'output_files/{input_file}.png') == 0:
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
        if jpg_txt.convert(f'input_files/{input_file}', f'output_files/{input_file}.txt') == 0:
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