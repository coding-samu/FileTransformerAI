from utils.utils_pdf import pdf
from utils.utils_jpg import jpg
from utils.utils_png import png
from utils.utils_docx import docx
from utils.utils_xlsx import xlsx

def main():
    t = None
    while True:
        input_file = input("Inserisci il nome del file di input (o 'exit' per uscire): ")
        if input_file == 'exit':
            break
        
        # Estrai l'estensione del file
        conversion_type = input_file.split('.')[-1]

        messaggio = f"Conversione del file {conversion_type} completata con successo!"
        error = 1

        match conversion_type:
            case "txt":
                print("Conversione TXT non ancora supportata.")
                continue # TODO: Implementare la conversione di file TXT
            case "pdf":
                error = pdf(input_file)
            case "jpg":
                error = jpg(input_file)
            case "png":
                error = png(input_file)
            case "docx":
                error = docx(input_file)
            case "xlsx":
                error = xlsx(input_file)
            case "audio":
                print("Conversione audio non ancora supportata.")
                continue # TODO: Implementare la conversione di file audio
            case _:
                print("Tipo di conversione non supportato.")
                continue
        
        if error == 0:
            print(messaggio)
        else:
            print("Errore durante la conversione del file.")

if __name__ == "__main__":
    main()
