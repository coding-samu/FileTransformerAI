def get_xlsx_model(conversion_type):
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
        case "docx":
            print("Conversione DOCX non ancora supportata.")
            return None
        case "txt":
            print("Conversione txt non ancora supportata.")
            return None
        case "svg":
            print("Conversione SVG non ancora supportata.")
            return None
        case _:
            print("Tipo di conversione non supportato.")
            return None