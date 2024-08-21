from utils.utils_translate import translate
from utils.utils_pdf import pdf
from utils.utils_jpg import jpg

def main():
    t = None
    while True:
        input_file = input("Inserisci il nome del file di input (o 'exit' per uscire): ")
        if input_file == 'exit':
            break

        conversion_type = input("Inserisci il tipo di conversione o il tipo di file da convertire (translate, pdf, jpg, png, docx, xlsx, audio): ")
        messaggio = f"Conversione {conversion_type} completata con successo!"
        error = 1

        match conversion_type:
            case "translate":
                error = translate(input_file)
            case "pdf":
                error = pdf(input_file)
            case "jpg":
                error = jpg(input_file)
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
        
        if error == 0:
            print(messaggio)
        else:
            print("Errore durante la conversione del file.")

if __name__ == "__main__":
    main()
