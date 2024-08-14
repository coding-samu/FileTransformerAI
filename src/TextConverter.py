from transformers import pipeline

class translation_en_to_fr:
    def __init__(self):
        # Inizializza un modello pre-addestrato di Hugging Face
        self.model = pipeline("translation_en_to_fr")

    def convert(self, input_text):
        max_length = 100000
        
        # Esegue la traduzione con max_length dinamico
        return self.model(input_text, max_length=max_length)[0]['translation_text']