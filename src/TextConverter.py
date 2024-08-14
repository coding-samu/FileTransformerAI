from transformers import MarianMTModel, MarianTokenizer

class translation_en_to_fr:
    def __init__(self):
        # Inizializza il tokenizer e il modello per la traduzione inglese-francese
        self.tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-fr")
        self.model = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-fr")

    def convert(self, input_text):
        # Tokenizza il testo di input
        inputs = self.tokenizer(input_text, return_tensors="pt", padding=True)
        
        # Genera la traduzione
        translated_tokens = self.model.generate(**inputs, max_length=10000)
        
        # Decodifica i token generati in testo
        translated_text = self.tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
        
        return translated_text
    
class translation_en_to_de:
    def __init__(self):
        # Inizializza il tokenizer e il modello per la traduzione inglese-tedesco
        self.tokenizer = MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-de")
        self.model = MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-en-de")

    def convert(self, input_text):
        # Tokenizza il testo di input
        inputs = self.tokenizer(input_text, return_tensors="pt", padding=True)
        
        # Genera la traduzione
        translated_tokens = self.model.generate(**inputs, max_length=1024)
        
        # Decodifica i token generati in testo
        translated_text = self.tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
        
        return translated_text

"""    
class UniversalTranslator:
    def __init__(self, source_lang, target_lang):
        # Costruisci il nome della pipeline di traduzione
        translation_task = f"translation_{source_lang}_to_{target_lang}"

        # Inizializza un tokenizer per mBART
        self.tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
        self.model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
        self.translation_pipeline = pipeline(translation_task, model=self.model, tokenizer=self.tokenizer)

    def convert(self, input_text):
        return self.translation_pipeline(input_text, max_length=1024, truncation=False)[0]['translation_text']
"""