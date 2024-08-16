from utils.utils_file import save_file_pdf
from ai_model.ai_model_pdf import PDFOCR

def get_pdf_model(conversion_type, input_file):
    match conversion_type:
        case "pdf_with_ocr":
            pdf_to_ocr(input_file)
        case "jpg":
            print("Conversione JPG non ancora supportata.")
            return None
        case "png":
            print("Conversione PNG non ancora supportata.")
            return None
        case "docx":
            print("Conversione DOCX non ancora supportata.")
            return None
        case "xlsx":
            print("Conversione XLSX non ancora supportata.")
            return None
        case "txt":
            print("Conversione txt non ancora supportata.")
            return None
        case "svg":
            print("Conversione SVG non ancora supportata.")
            return None
        case "compress":
            print("Compressione PDF non ancora supportata.")
            return None
        case "txt_summary":
            print("Riassunto non ancora supportato.")
            return None
        case _:
            print("Tipo di conversione non supportato.")
            return None

def get_type_conversion():
    print("Inserisci il tipo di conversione o il tipo di file da convertire (pdf_with_ocr, jpg, png, docx, xlsx, txt, svg, compress, txt_summary): ")
    return input()

def pdf_to_ocr(input_file):
    try:
        pdf_ocr = PDFOCR()
        pdf_writer = pdf_ocr.convert(f'input_files/{input_file}', f'output_files/({input_file}_ocr)')
        save_file_pdf(pdf_writer, f'output_files/({input_file}_ocr)')
        print(f"Salvataggio completato!")
    except Exception as e:
        print(f"Errore durante la conversione del file {input_file}: {e}")

def pdf(input_file):
    conversion_type = get_type_conversion()
    get_pdf_model(conversion_type, input_file)