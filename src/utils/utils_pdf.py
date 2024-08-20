from utils.utils_file import save_file_pdf, save_file_docx, save_file_txt
from ai_model.ai_model_pdf import PDFOCR, PDFDOCX, PDFJPG, PDFPNG, PDFXLSX, PDFTXT, PDFSVG, PDFCOMPRESS, PDFTXTSUMMARY

def get_pdf_model(conversion_type, input_file):
    match conversion_type:
        case "ocr":
            pdf_to_ocr(input_file)
        case "jpg":
            pdf_to_jpg(input_file)
        case "png":
            pdf_to_png(input_file)
        case "docx":
            pdf_to_docx(input_file)
        case "xlsx":
            pdf_to_xlsx(input_file)
        case "txt":
            pdf_to_txt(input_file)
        case "svg":
            pdf_to_svg(input_file)
        case "compress":
            pdf_compress(input_file)
        case "txt_summary":
            pdf_txt_summary(input_file)
        case _:
            print("Tipo di conversione non supportato.")
            return None

def get_type_conversion():
    print("Inserisci il tipo di conversione o il tipo di file da convertire (ocr, jpg, png, docx, xlsx, txt, svg, compress, txt_summary): ")
    return input()

def pdf_to_ocr(input_file):
    try:
        pdf_ocr = PDFOCR()
        pdf_writer = pdf_ocr.convert(f'input_files/{input_file}')
        save_file_pdf(pdf_writer, f'output_files/ocr_{input_file}')
        print(f"Salvataggio completato!")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")

def pdf_to_jpg(input_file):
    print("Conversione JPG non ancora supportata.")
    # TODO: implementare la conversione da PDF a JPG

def pdf_to_png(input_file):
    print("Conversione PNG non ancora supportata.")
    # TODO: implementare la conversione da PDF a PNG

def pdf_to_docx(input_file):
    try:
        pdf_docx = PDFDOCX()
        txt = pdf_docx.convert(f'input_files/{input_file}')
        save_file_docx(txt, f'output_files/{input_file}.docx')
        print(f"Salvataggio completato!")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")


def pdf_to_xlsx(input_file):
    print("Conversione XLSX non ancora supportata.")
    # TODO: implementare la conversione da PDF a XLSX

def pdf_to_txt(input_file):
    try:
        pdf_txt = PDFTXT()
        txt = pdf_txt.convert(f'input_files/{input_file}')
        save_file_txt(txt, f'output_files/{input_file}.txt')
        print(f"Salvataggio completato!")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")

def pdf_to_svg(input_file):
    try:
        page_number = int(input("Inserisci il numero di pagina da convertire in SVG: "))
        pdf_svg = PDFSVG()
        if pdf_svg.convert_to_svg(f'input_files/{input_file}', f'output_files/{input_file}.svg', page_number) == 0:
            print(f"Salvataggio completato!")
        else:
            raise Exception("Errore durante la conversione del file {input_file}")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")

def pdf_compress(input_file):
    try:
        pdf_compress = PDFCOMPRESS()
        pdf_compress.compress(f'input_files/{input_file}', f'output_files/compressed_{input_file}')
        print(f"Salvataggio completato!")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")

def pdf_txt_summary(input_file):
    try:
        pdf_txt_summary = PDFTXTSUMMARY()
        summary = pdf_txt_summary.summarize(f'input_files/{input_file}')
        save_file_txt(summary, f'output_files/summary_{input_file}.txt')
        print(f"Salvataggio completato!")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")

def pdf(input_file):
    conversion_type = get_type_conversion()
    get_pdf_model(conversion_type, input_file)