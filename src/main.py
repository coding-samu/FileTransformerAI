from utils.utils_txt import txt
from utils.utils_pdf import pdf
from utils.utils_jpg import jpg
from utils.utils_png import png
from utils.utils_docx import docx
from utils.utils_xlsx import xlsx
from utils.utils_mp3 import mp3

def main():
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
                error = txt(input_file)
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
            case "mp3":
                error = mp3(input_file)
            case _:
                print("Tipo di conversione non supportato.")
                continue
        
        if error == 0:
            print(messaggio)
        else:
            print("Errore durante la conversione del file.")

if __name__ == "__main__":
    print("Avvio in corso...")
    main()
