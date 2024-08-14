from ai_model import get_converter
from utils import load_file, save_file

def main():
    while True:
        input_file = input("Inserisci il nome del file di input (o 'exit' per uscire): ")
        if input_file == 'exit':
            break

        conversion_type = input("Inserisci il tipo di conversione (text_en_to_fr, text_en_to_de, text_it_to_en, better_image): ")

        if conversion_type.startswith('text_'):
            input_data = load_file(f'input_files/{input_file}', mode='text')
        elif conversion_type == 'better_image':
            input_data = load_file(f'input_files/{input_file}', mode='image')
        else:
            print("Tipo di conversione non supportato.")
            continue

        converter = get_converter(conversion_type)
        output_data = converter.convert(input_data)

        if conversion_type.startswith('text_'):
            save_file(output_data, f'output_files/{input_file}', mode='text')
        elif conversion_type == 'better_image':
            save_file(output_data, f'output_files/{input_file}', mode='image')

        print(f"Conversione {conversion_type} completata con successo!")

if __name__ == "__main__":
    main()
