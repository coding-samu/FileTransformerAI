from transformers import pipeline, AutoTokenizer

class translation_en_to_fr:
    def __init__(self):
        # Inizializza il tokenizer con una lunghezza massima personalizzata
        self.tokenizer = AutoTokenizer.from_pretrained("t5-base", model_max_length=100000)
        # Inizializza un modello pre-addestrato di Hugging Face
        self.model = pipeline("translation_en_to_fr")

    def convert(self, input_text):
        # Esegue la traduzione con max_length=100000 per evitare la limitazione di lunghezza
        return self.model(input_text, max_length=100000, truncation=False)[0]['translation_text']
    
class translation_en_to_de:
    def __init__(self):
        # Inizializza il tokenizer con una lunghezza massima personalizzata
        self.tokenizer = AutoTokenizer.from_pretrained("t5-base", model_max_length=100000)
        # Inizializza un modello pre-addestrato di Hugging Face
        self.model = pipeline("translation_en_to_de")

    def convert(self, input_text):
        # Esegue la traduzione con max_length=100000 per evitare la limitazione di lunghezza
        return self.model(input_text, max_length=100000, truncation=False)[0]['translation_text']
    