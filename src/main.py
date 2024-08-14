import sys
from utils import load_file, save_file
from ai_model import get_converter

def main():
    while True:
        input_file = input("Inserisci il nome del file di input (o 'exit' per uscire): ")
        if input_file.lower() == 'exit':
            print("Uscita dal programma.")
            break

        conversion_type = input("Inserisci il tipo di conversione (text_en_to_fr, text_en_to_de, text_it_to_en, better_image): ")

        # Carica il file di input
        try:
            input_data = load_file(f'input_files/{input_file}')
        except FileNotFoundError:
            print(f"File '{input_file}' non trovato. Riprova.")
            continue

        # Ottieni il convertitore giusto basato sul tipo di conversione
        converter = get_converter(conversion_type)
        if converter is None:
            print(f"Tipo di conversione '{conversion_type}' non supportato.")
            continue

        # Esegui la conversione
        output_data = converter.convert(input_data)

        # Salva il file di output
        output_file = f"output_files/converted_{conversion_type}_{input_file}"
        save_file(output_data, output_file)
        print(f"Conversione completata: {output_file}")

if __name__ == "__main__":
    main()
