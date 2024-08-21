from utils.utils_file import save_file_pdf, save_file_docx, save_file_txt
from ai_model.ai_model_pdf import PDFOCR, PDFDOCX, PDFJPG, PDFPNG, PDFXLSX, PDFTXT, PDFSVG, PDFCOMPRESS, PDFTXTSUMMARY

def get_pdf_model(conversion_type, input_file):
    match conversion_type:
        case "ocr":
            return pdf_to_ocr(input_file)
        case "jpg":
            return pdf_to_jpg(input_file)
        case "png":
            return pdf_to_png(input_file)
        case "docx":
            return pdf_to_docx(input_file)
        case "xlsx":
            return pdf_to_xlsx(input_file)
        case "txt":
            return pdf_to_txt(input_file)
        case "svg":
            return pdf_to_svg(input_file)
        case "compress":
            return pdf_compress(input_file)
        case "txt_summary":
            return pdf_txt_summary(input_file)
        case _:
            print("Tipo di conversione non supportato.")
            return 1

def get_type_conversion():
    print("Come desideri convertire il file PDF? (ocr, jpg, png, docx, xlsx, txt, svg, compress, txt_summary): ")
    return input()

def pdf_to_ocr(input_file):
    try:
        pdf_ocr = PDFOCR()
        if pdf_ocr.convert(f'input_files/{input_file}', f'output_files/ocr_{input_file}') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1

def pdf_to_jpg(input_file):
    try:
        page_number = int(input("Inserisci il numero di pagina da convertire in JPG: "))
        pdf_jpg = PDFJPG()
        if pdf_jpg.convert(f'input_files/{input_file}', f'output_files/{input_file}.jpg', page_number) == 0:
            print(f"Salvataggio completato!")
        else:
            raise Exception("Errore durante la conversione del file")
        return 0
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1

def pdf_to_png(input_file):
    try:
        page_number = int(input("Inserisci il numero di pagina da convertire in PNG: "))
        pdf_png = PDFPNG()
        if pdf_png.convert(f'input_files/{input_file}', f'output_files/{input_file}.png', page_number) == 0:
            print(f"Salvataggio completato!")
        else:
            raise Exception("Errore durante la conversione del file")
        return 0
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1

def pdf_to_docx(input_file):
    try:
        pdf_docx = PDFDOCX()
        if pdf_docx.convert(f'input_files/{input_file}', f'output_files/{input_file}.docx') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1


def pdf_to_xlsx(input_file):
    try:
        page_number = int(input("Inserisci il numero di pagina da convertire in XLSX: "))
        pdf_xlsx = PDFXLSX()
        if pdf_xlsx.convert(f'input_files/{input_file}', f'output_files/{input_file}.xlsx', page_number) == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1
        
def pdf_to_txt(input_file):
    try:
        pdf_txt = PDFTXT()
        if pdf_txt.convert(f'input_files/{input_file}',f'output_files/{input_file}.txt') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1

def pdf_to_svg(input_file):
    try:
        page_number = int(input("Inserisci il numero di pagina da convertire in SVG: "))
        pdf_svg = PDFSVG()
        if pdf_svg.convert_to_svg(f'input_files/{input_file}', f'output_files/{input_file}.svg', page_number) == 0:
            print(f"Salvataggio completato!")
        else:
            raise Exception("Errore durante la conversione del file")
        return 0
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1

def pdf_compress(input_file):
    try:
        pdf_compress = PDFCOMPRESS()
        if pdf_compress.compress(f'input_files/{input_file}', f'output_files/compressed_{input_file}') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1

def pdf_txt_summary(input_file):
    try:
        pdf_txt_summary = PDFTXTSUMMARY()
        if pdf_txt_summary.summarize(f'input_files/{input_file}', f'output_files/summary_{input_file}.txt') == 0:
            print(f"Salvataggio completato!")
            return 0
        else:
            raise Exception("Errore durante la conversione del file")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")
        return 1

def pdf(input_file):
    conversion_type = get_type_conversion()
    return get_pdf_model(conversion_type, input_file)