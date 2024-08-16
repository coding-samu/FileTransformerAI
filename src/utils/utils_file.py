from PyPDF2 import PdfReader, PdfWriter

def load_file_txt(file_path):
    # verifica che l'estensione del file sia .txt
    if not file_path.endswith('.txt'):
        print(f"Estensione del file {file_path} non supportata.")
        return None
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Errore durante il caricamento del file {file_path}: {e}")
        return None

def save_file_txt(data, file_path):
    # verifica che l'estensione del file sia .txt
    if not file_path.endswith('.txt'):
        print(f"Estensione del file {file_path} non supportata.")
        return None
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
    except Exception as e:
        print(f"Errore durante il salvataggio del file {file_path}: {e}")
        return None
    
def load_file_pdf(file_path):
    # verifica che l'estensione del file sia .pdf
    if not file_path.endswith('.pdf'):
        print(f"Estensione del file {file_path} non supportata.")
        return None
    try:
        reader = PdfReader(file_path)
        return reader
    except Exception as e:
        print(f"Errore durante il caricamento del file {file_path}: {e}")
        return None
    
def save_file_pdf(pdf_writer, file_path):
    if not file_path.endswith('.pdf'):
        print(f"Estensione del file {file_path} non supportata.")
        return None
    if pdf_writer is None:
        print(f"Errore: il pdf_writer è None, non posso salvare il file.")
        return None
    try:
        with open(file_path, 'wb') as file:
            pdf_writer.write(file)
    except Exception as e:
        print(f"Errore durante il salvataggio del file {file_path}: {e}")
        return None