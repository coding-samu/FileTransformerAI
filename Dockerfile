# Usa un'immagine Python come base
FROM python:3.9-slim

# Setta la directory di lavoro all'interno del container
WORKDIR /app

# Copia i file di requirements e installa le dipendenze
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il codice nel container
COPY . .

# Comando per eseguire il programma
CMD ["python", "src/main.py"]
