# Usa un'immagine di base compatibile con PyTorch e OpenCV
FROM python:3.10-slim

# Installazione delle dipendenze di sistema
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    poppler-utils \
    tesseract-ocr \
    tesseract-ocr-ita \
    && rm -rf /var/lib/apt/lists/*

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file di requisiti e installa le dipendenze Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice sorgente
COPY src/ ./src/
COPY models/ ./models/

# Esponi la porta 8000 (se hai bisogno di un servizio web, altrimenti puoi rimuoverlo)
EXPOSE 8000

# Comando di default per mantenere il container attivo
CMD ["tail", "-f", "/dev/null"]
