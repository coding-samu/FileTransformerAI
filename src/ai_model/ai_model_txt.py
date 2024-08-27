from ai_model.ai_model_translate import UniversalTranslator
from ai_model.ai_model_docx import DOCXPDF
from utils.utils_file import load_file_txt, save_file_txt, save_file_pdf, save_file_docx, save_file_jpg, save_file_png
import os
import shutil
import io
from PIL import Image, ImageDraw, ImageFont
from transformers import BartTokenizer, BartForConditionalGeneration
from io import BytesIO

import torch
from diffusers import StableDiffusionPipeline

class TXTPDF:
    def __init__(self):
        pass

    def convert(self, input_txt_path, output_pdf_path):
        try:
            # Converti il file txt in docx utilizzando la classe TXTDOCX
            txt_docx = TXTDOCX()
            # Creazione del percorso del file temporaneo docx
            output_docx_path = f'temp_file/{input_txt_path}.docx'
            # Crea le cartelle necessarie
            os.makedirs(os.path.dirname(output_docx_path), exist_ok=True)
            if txt_docx.convert(input_txt_path, output_docx_path) == 1:
                raise Exception(f"Errore durante la conversione del file {input_txt_path}")
            # Converti il file docx in pdf utilizzando la classe DOCXPDF
            docx_pdf = DOCXPDF()
            if docx_pdf.convert(output_docx_path, output_pdf_path) == 0:
                print(f"Salvataggio completato!")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file PDF: {output_pdf_path}")
        except Exception as e:
            print(f"Errore durante la conversione del file {input_txt_path}: {e}")
            return 1
        finally:
            try:
                # Elimina la cartella temporanea e tutto il suo contenuto
                shutil.rmtree('temp_file')
                print(f"Cartella temporanea eliminata: temp_file")
            except Exception as e:
                print(f"Errore durante l'eliminazione della cartella temporanea: temp_file. Dettagli: {e}")

class TXTJPG:
    def __init__(self):
        pass

    def convert(self, input_txt_path, output_jpg_path):
        try:
            # Carica il contenuto del file TXT
            with open(input_txt_path, 'r', encoding='utf-8') as file:
                text = file.read()

            # Configurazione dell'immagine
            font = ImageFont.load_default()  # Usa il font di default
            lines = text.split('\n')

            # Calcola la larghezza massima e l'altezza totale del testo
            max_width = 800  # Larghezza massima dell'immagine
            line_height = font.getbbox('A')[3]  # Altezza della riga basata sul font
            total_height = line_height * len(lines) + 20  # Altezza totale dell'immagine con padding

            # Crea l'immagine con le dimensioni calcolate
            image = Image.new('RGB', (max_width, total_height), color='white')
            draw = ImageDraw.Draw(image)

            # Scrivi il testo nell'immagine
            y_text = 10  # Padding superiore
            for line in lines:
                width, height = draw.textbbox((0, 0), line, font=font)[2:4]
                draw.text(((max_width - width) / 2, y_text), line, font=font, fill="black")
                y_text += height

            # Salva l'immagine come JPG
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='JPEG')
            img_data = img_byte_arr.getvalue()

            # Usa la funzione save_file_jpg per salvare il file
            if save_file_jpg(img_data, output_jpg_path) == 0:
                print(f"Conversione completata: {output_jpg_path}")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file JPG: {output_jpg_path}")

        except Exception as e:
            print(f"Errore durante la conversione del file {input_txt_path}: {e}")
            return 1

class TXTPNG:
    def __init__(self):
        pass

    def convert(self, input_txt_path, output_png_path):
        try:
            # Carica il contenuto del file TXT
            with open(input_txt_path, 'r', encoding='utf-8') as file:
                text = file.read()

            # Configurazione dell'immagine
            font = ImageFont.load_default()  # Usa il font di default
            lines = text.split('\n')

            # Calcola la larghezza massima e l'altezza totale del testo
            max_width = 800  # Larghezza massima dell'immagine
            line_height = font.getbbox('A')[3]  # Altezza della riga basata sul font
            total_height = line_height * len(lines) + 20  # Altezza totale dell'immagine con padding

            # Crea l'immagine con le dimensioni calcolate
            image = Image.new('RGB', (max_width, total_height), color='white')
            draw = ImageDraw.Draw(image)

            # Scrivi il testo nell'immagine
            y_text = 10  # Padding superiore
            for line in lines:
                width, height = draw.textbbox((0, 0), line, font=font)[2:4]
                draw.text(((max_width - width) / 2, y_text), line, font=font, fill="black")
                y_text += height

            # Salva l'immagine come PNG
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='PNG')
            img_data = img_byte_arr.getvalue()

            # Usa la funzione save_file_png per salvare il file
            if save_file_png(img_data, output_png_path) == 0:
                print(f"Conversione completata: {output_png_path}")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file PNG: {output_png_path}")

        except Exception as e:
            print(f"Errore durante la conversione del file {input_txt_path}: {e}")
            return 1

class TXTDOCX:
    def __init__(self):
        pass

    def convert(self, input_txt_path, output_docx_path):
        try:
            text = load_file_txt(input_txt_path)
            if text == 1:
                raise Exception(f"Errore durante il caricamento del file TXT: {input_txt_path}")
            if save_file_docx(text, output_docx_path) == 0:
                print(f"Salvataggio completato!")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file DOCX: {output_docx_path}")
        except Exception as e:
            print(f"Errore durante la conversione del file {input_txt_path}: {e}")
            return 1

class TXTSpeech:
    pass # TODO: Implementare la conversione di file TXT in file audio

class TXTTranslate:
    def __init__(self, source_language, target_language):
        self.translator = UniversalTranslator(source_language, target_language)
    
    def convert(self, input_txt_path, output_txt_path):
        try:
            text = load_file_txt(input_txt_path)
            if text == 1:
                raise Exception(f"Errore durante il caricamento del file TXT: {input_txt_path}")
            translated_text = self.translator.convert(text)
            if save_file_txt(translated_text, output_txt_path) == 0:
                print(f"Salvataggio completato!")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file TXT: {output_txt_path}")
        except Exception as e:
            print(f"Errore durante la conversione del file {input_txt_path}: {e}")
            return 1
        
class TXTSummary:
    def __init__(self):
        # Inizializza il modello e il tokenizer per il riassunto
        self.tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
        self.model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

    def convert(self, input_txt_path, output_txt_path):
        try:
            # Carica il file TXT
            text = load_file_txt(input_txt_path)

            # Preprocessa il testo per il modello
            inputs = self.tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)

            # Genera il riassunto
            summary_ids = self.model.generate(
                inputs["input_ids"],
                max_length=150,
                min_length=0,
                length_penalty=2.0,
                num_beams=4,
                early_stopping=True
            )

            # Decodifica il riassunto generato
            summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)

            # Salva il riassunto nel file TXT
            if save_file_txt(summary, output_txt_path) == 0:
                print(f"Riassunto completato e salvato in: {output_txt_path}")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio del file TXT: {output_txt_path}")

        except Exception as e:
            print(f"Errore durante la conversione del file {input_txt_path}: {e}")
            return 1

class TXTImageGen:
    def __init__(self, model_name="stabilityai/stable-diffusion-2-1", safety_checker=True):
        try:
            print("Caricamento del modello di generazione immagini (questa operazione potrebbe richiedere diversi minuti)...")
            
            # Inizializza la pipeline di Stable Diffusion
            self.pipe = StableDiffusionPipeline.from_pretrained(
                model_name,
                torch_dtype=torch.float32
            )
            
            # Disabilita il safety checker se necessario
            if not safety_checker:
                self.pipe.safety_checker = lambda images, **kwargs: (images, False)
            
            # Imposta la pipeline sulla CPU
            self.pipe = self.pipe.to("cpu")
            
            print("Modello caricato correttamente sulla CPU.")
        except Exception as e:
            print(f"Errore durante il caricamento del modello: {e}")
            raise

    def convert(self, input_txt_path, output_img_path, num_inference_steps=50, guidance_scale=7.5):
        try:
            # Carica la descrizione dal file di testo
            description = load_file_txt(input_txt_path).strip()
            if not description:
                raise ValueError("Il file di testo di input è vuoto.")
            
            print(f"Descrizione caricata: {description}")
            print("Inizio generazione dell'immagine (questo potrebbe richiedere diversi minuti)...")
            
            # Genera l'immagine
            with torch.no_grad():
                output = self.pipe(
                    description,
                    num_inference_steps=num_inference_steps,
                    guidance_scale=guidance_scale
                )
                image = output.images[0]
            
            # Converti l'immagine in formato bytes-like
            img_byte_arr = BytesIO()
            image.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()
            
            # Salva l'immagine utilizzando save_file_jpg
            if save_file_jpg(img_byte_arr, output_img_path) == 0:
                print(f"Immagine generata e salvata in: {output_img_path}")
                return 0
            else:
                raise Exception(f"Errore durante il salvataggio dell'immagine: {output_img_path}")
        except Exception as e:
            print(f"Errore durante la conversione del file {input_txt_path}: {e}")
            return 1

class TXTWrite:
    pass # TODO: Implementare la scrittura di testo in file TXT