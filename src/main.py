import sys
from utils import load_file, save_file
from ai_model import get_converter

def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <input_file> <conversion_type>")
        sys.exit(1)

    input_file = sys.argv[1]
    conversion_type = sys.argv[2]

    # Carica il file di input
    input_data = load_file(input_file)

    # Ottieni il convertitore giusto basato sul tipo di conversione
    converter = get_converter(conversion_type)
    if converter is None:
        print(f"Conversion type '{conversion_type}' not supported.")
        sys.exit(1)

    # Esegui la conversione
    output_data = converter.convert(input_data)

    # Salva il file di output
    output_file = f"output_files/converted_{conversion_type}_{input_file.split('/')[-1]}"
    save_file(output_data, output_file)
    print(f"Conversione completata: {output_file}")

if __name__ == "__main__":
    main()
