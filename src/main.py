from utils_translate import translate

def main():
    t = None
    while True:
        input_file = input("Inserisci il nome del file di input (o 'exit' per uscire): ")
        if input_file == 'exit':
            break

        conversion_type = input("Inserisci il tipo di conversione (translate, pdf, jpg, png): ")

        match conversion_type:
            case "translate":
                translate(input_file)
            case "pdf":
                print("Conversione PDF non ancora supportata.")
                continue
            case "jpg":
                print("Conversione JPG non ancora supportata.")
                continue
            case "png":
                print("Conversione PNG non ancora supportata.")
                continue
            case _:
                print("Tipo di conversione non supportato.")
                continue

        print(f"Conversione {conversion_type} completata con successo!")

if __name__ == "__main__":
    main()
