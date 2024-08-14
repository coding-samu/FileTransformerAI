from transformers import MarianMTModel, MarianTokenizer

class UniversalTranslator:
    def __init__(self, source_lang, target_lang):
        # Costruisci il nome della pipeline di traduzione
        translation_task = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"

        # Inizializza il tokenizer e il modello per la traduzione italiano-inglese
        self.tokenizer = MarianTokenizer.from_pretrained(translation_task)
        self.model = MarianMTModel.from_pretrained(translation_task)

    def convert(self, input_text):
        # Tokenizza il testo di input
        inputs = self.tokenizer(input_text, return_tensors="pt", padding=True)
        
        # Genera la traduzione
        translated_tokens = self.model.generate(**inputs, max_length=1024)
        
        # Decodifica i token generati in testo
        translated_text = self.tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

        return translated_text