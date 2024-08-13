from transformers import pipeline

class TextConverter:
    def __init__(self):
        # Inizializza un modello pre-addestrato di Hugging Face
        self.model = pipeline("translation_en_to_fr")

    def convert(self, input_text):
        # Esegue la traduzione
        return self.model(input_text)[0]['translation_text']
