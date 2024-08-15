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