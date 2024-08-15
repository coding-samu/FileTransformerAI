def get_jpg_model(conversion_type):
    match conversion_type:
        case "pdf":
            print("Conversione PDF non ancora supportata.")
            return None
        case "png":
            print("Conversione PNG non ancora supportata.")
            return None
        case "txt":
            print("Estrazione del testo in un file txt non ancora supportata.")
            return None
        case _:
            print("Tipo di conversione non supportato.")
            return None