# Usa un'immagine Python ufficiale
FROM python:3.10-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia i file di progetto nella directory di lavoro
COPY . .

# Installa le dipendenze
RUN pip install --no-cache-dir -r requirements.txt

# Esponi la porta 8000 (se hai bisogno di un servizio web, altrimenti puoi rimuoverlo)
EXPOSE 8000

# Comando di default per mantenere il container attivo
CMD ["tail", "-f", "/dev/null"]
