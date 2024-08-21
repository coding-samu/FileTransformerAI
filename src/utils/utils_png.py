def get_png_model(conversion_type):
    match conversion_type:
        case "pdf":
            print("Conversione PDF non ancora supportata.")
            return None
        case "jpg":
            print("Conversione JPG non ancora supportata.")
            return None
        case "txt":
            print("Estrazione del testo in un file txt non ancora supportata.")
            return None
        case _:
            print("Tipo di conversione non supportato.")
            return None
        
def get_type_conversion():
    print("Come desideri convertire il file PNG? (pdf, jpg, txt): ")
    return input()

def png(input_file):
    conversion_type = get_type_conversion()
    return get_png_model(conversion_type)

def png_to_pdf(input_file):
    try:
        png_pdf = PNGPDF()
        if png_pdf.convert(f'input_files/{input_file}', f'output_files/{input_file}.pdf') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1

def png_to_jpg(input_file):
    try:
        png_jpg = PNGJPG()
        if png_jpg.convert(f'input_files/{input_file}', f'output_files/{input_file}.jpg') == 0:
            print(f"Salvataggio completato!")
        else:
            raise Exception("Errore durante la conversione del file")
        return 0
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1

def png_to_txt(input_file):
    try:
        png_txt = PNGTXT()
        if png_txt.convert(f'input_files/{input_file}', f'output_files/{input_file}.txt') == 0:
            print(f"Salvataggio completato!")
        else:
            raise Exception("Errore durante la conversione del file")
        return 0
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1