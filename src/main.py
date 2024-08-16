from utils.utils_translate import translate
from utils.utils_pdf import pdf

def main():
    t = None
    while True:
        input_file = input("Inserisci il nome del file di input (o 'exit' per uscire): ")
        if input_file == 'exit':
            break

        conversion_type = input("Inserisci il tipo di conversione o il tipo di file da convertire (translate, pdf, jpg, png, docx, xlsx, audio): ")

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
            case "docx":
                print("Conversione DOCX non ancora supportata.")
                continue
            case "xlsx":
                print("Conversione XLSX non ancora supportata.")
                continue
            case "audio":
                print("Conversione audio non ancora supportata.")
                continue
            case _:
                print("Tipo di conversione non supportato.")
                continue

        print(f"Conversione {conversion_type} completata con successo!")

if __name__ == "__main__":
    main()
