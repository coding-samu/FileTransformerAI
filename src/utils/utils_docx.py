def get_docx_model(conversion_type):
    match conversion_type:
        case "pdf":
            print("Conversione PDF non ancora supportata.")
            return None
        case "jpg":
            print("Conversione JPG non ancora supportata.")
            return None
        case "png":
            print("Conversione PNG non ancora supportata.")
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
        case "txt_summary":
            print("Riassunto non ancora supportato.")
            return None
        case _:
            print("Tipo di conversione non supportato.")
            return None