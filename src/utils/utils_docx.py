from ai_model.ai_model_docx import DOCXPDF, DOCXJPG, DOCXPNG, DOCXXLSX, DOCXTXT, DOCXSVG, DOCXTXTSummary, DOCXTranslate
from utils.utils_translate import get_languages

import os

def get_docx_model(conversion_type, input_file):
    match conversion_type:
        case "pdf":
            return docx_to_pdf(input_file)
        case "jpg":
            return docx_to_jpg(input_file)
        case "png":
            return docx_to_png(input_file)
        case "xlsx":
            return docx_to_xlsx(input_file)
        case "txt":
            return docx_to_txt(input_file)
        case "svg":
            return docx_to_svg(input_file)
        case "txt_summary":
            return docx_to_txt_summary(input_file)
        case "translate":
            return docx_translate(input_file)
        case _:
            print("Tipo di conversione non supportato.")
            return 1
        
def get_type_conversion():
    print("Come desideri convertire il file DOCX? (pdf, jpg, png, xlsx, txt, svg, txt_summary, translate): ")
    return input()

def docx(input_file):
    conversion_type = get_type_conversion()
    return get_docx_model(conversion_type, input_file)

def docx_to_pdf(input_file):
    try:
        docx_pdf = DOCXPDF()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if docx_pdf.convert(f'input_files/{input_file}', f'output_files/{base_name}.pdf') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1
    
def docx_to_jpg(input_file):
    try:
        page_number = int(input("Inserisci il numero di pagina da convertire in JPG: "))
        docx_jpg = DOCXJPG()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if docx_jpg.convert(f'input_files/{input_file}', f'output_files/{base_name}.jpg', page_number) == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1
    
def docx_to_png(input_file):
    try:
        page_number = int(input("Inserisci il numero di pagina da convertire in PNG: "))
        docx_png = DOCXPNG()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if docx_png.convert(f'input_files/{input_file}', f'output_files/{base_name}.png', page_number) == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1
    
def docx_to_xlsx(input_file):
    try:
        docx_xlsx = DOCXXLSX()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if docx_xlsx.convert(f'input_files/{input_file}', f'output_files/{base_name}.xlsx') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1
    
def docx_to_txt(input_file):
    try:
        docx_txt = DOCXTXT()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if docx_txt.convert(f'input_files/{input_file}', f'output_files/{base_name}.txt') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1

def docx_to_svg(input_file):
    try:
        page_number = int(input("Inserisci il numero di pagina da convertire in SVG: "))
        docx_svg = DOCXSVG()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if docx_svg.convert(f'input_files/{input_file}', f'output_files/{base_name}.svg', page_number) == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1
    
def docx_to_txt_summary(input_file):
    try:
        docx_txt_summary = DOCXTXTSummary()
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if docx_txt_summary.convert(f'input_files/{input_file}', f'output_files/{base_name}_summary.txt') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1
    
def docx_translate(input_file):
    try:
        T = get_languages()
        docx_translate = DOCXTranslate(T[0], T[1])
        # Rimuovi l'estensione esistente dal file di input
        base_name = os.path.splitext(input_file)[0]
        if docx_translate.convert(f'input_files/{input_file}', f'output_files/{base_name}_translated.docx') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1