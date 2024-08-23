from ai_model.ai_model_xlsx import XLSXPDF, XLSXJPG, XLSXPNG, XLSXDOCX, XLSXTXT, XLSXSVG

import os

def get_xlsx_model(conversion_type, input_file):
    match conversion_type:
        case "pdf":
            return xlsx_to_pdf(input_file)
        case "jpg":
            return xlsx_to_jpg(input_file)
        case "png":
            return xlsx_to_png(input_file)
        case "docx":
            return xlsx_to_docx(input_file)
        case "txt":
            return xlsx_to_txt(input_file)
        case "svg":
            return xlsx_to_svg(input_file)
        case _:
            print("Tipo di conversione non supportato.")
            return 1
        
def get_type_conversion():
    print("Come desideri convertire il file XLSX? (pdf, jpg, png, docx, txt, svg): ")
    return input()

def xlsx(input_file):
    conversion_type = get_type_conversion()
    return get_xlsx_model(conversion_type, input_file)

def xlsx_to_pdf(input_file):
    try:
        xlsx_pdf = XLSXPDF()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if xlsx_pdf.convert(f'input_files/{input_file}', f'output_files/{base_name}.pdf') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1
    
def xlsx_to_jpg(input_file):
    try:
        page_number = int(input("Inserisci il numero di pagina da convertire in JPG: "))
        xlsx_jpg = XLSXJPG()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if xlsx_jpg.convert(f'input_files/{input_file}', f'output_files/{base_name}.jpg', page_number) == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1
    
def xlsx_to_png(input_file):
    try:
        page_number = int(input("Inserisci il numero di pagina da convertire in PNG: "))
        xlsx_png = XLSXPNG()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if xlsx_png.convert(f'input_files/{input_file}', f'output_files/{base_name}.png', page_number) == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1
    
def xlsx_to_docx(input_file):
    try:
        xlsx_docx = XLSXDOCX()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if xlsx_docx.convert(f'input_files/{input_file}', f'output_files/{base_name}.docx') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1
    
def xlsx_to_txt(input_file):
    try:
        xlsx_txt = XLSXTXT()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if xlsx_txt.convert(f'input_files/{input_file}', f'output_files/{base_name}.txt') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1
    
def xlsx_to_svg(input_file):
    try:
        page_number = int(input("Inserisci il numero di pagina da convertire in SVG: "))
        xlsx_svg = XLSXSVG()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if xlsx_svg.convert(f'input_files/{input_file}', f'output_files/{base_name}.svg', page_number) == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1