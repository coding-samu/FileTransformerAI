import torch
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

from utils.utils_file import save_file_txt

class MP3STT:
    def __init__(self, lang='en'):
        # Seleziona il modello basato sulla lingua specificata
        self.lang = lang
        self.model_name = self._select_model(lang)
        self.processor = Wav2Vec2Processor.from_pretrained(self.model_name)
        self.model = Wav2Vec2ForCTC.from_pretrained(self.model_name)

    def _select_model(self, lang):
        # Seleziona il modello corretto in base alla lingua
        model_map = {
            'en': 'facebook/wav2vec2-large-960h',       # Inglese
            'it': 'facebook/wav2vec2-large-xlsr-53-italian', # Italiano
            'es': 'facebook/wav2vec2-large-xlsr-53-spanish', # Spagnolo
            'fr': 'facebook/wav2vec2-large-xlsr-53-french',  # Francese
            'de': 'facebook/wav2vec2-large-xlsr-53-german',  # Tedesco
        }
        return model_map.get(lang, 'facebook/wav2vec2-large-960h')  # Default inglese

    def convert(self, input_mp3_path, output_txt_path):
        try:
            # Carica l'audio dal file MP3
            waveform, sample_rate = torchaudio.load(input_mp3_path)

            # Resample se necessario
            if sample_rate != 16000:
                waveform = torchaudio.transforms.Resample(sample_rate, 16000)(waveform)

            # Preprocessa l'audio
            inputs = self.processor(waveform.squeeze(), sampling_rate=16000, return_tensors="pt", padding=True)

            # Genera la trascrizione
            with torch.no_grad():
                logits = self.model(inputs.input_values).logits
            predicted_ids = torch.argmax(logits, dim=-1)
            transcription = self.processor.decode(predicted_ids[0])

            # Salva la trascrizione nel file TXT
            if save_file_txt(transcription, output_txt_path) == 0:
                print(f"Trascrizione completata e salvata in: {output_txt_path}")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file TXT: {output_txt_path}")

        except Exception as e:
            print(f"Errore durante la conversione del file {input_mp3_path}: {e}")
            return 1