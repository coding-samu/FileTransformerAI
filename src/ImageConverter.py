import torch
from PIL import Image
import timm
import io
import numpy as np

class better_image:
    def __init__(self):
        # Inizializza il modello SwinIR utilizzando timm
        self.model = timm.create_model('swinir_large', pretrained=True)
        self.model.eval()  # Imposta il modello in modalità valutazione

    def convert(self, input_image_path):
        # Carica l'immagine usando PIL
        image = Image.open(input_image_path).convert("RGB")
        
        # Pre-processamento dell'immagine
        transform = timm.data.transforms_factory.transforms_imagenet_eval(
            img_size=self.model.default_cfg['input_size'][1]
        )
        input_tensor = transform(image).unsqueeze(0)  # Aggiungi la dimensione del batch

        # Inference
        with torch.no_grad():
            output = self.model(input_tensor)

        # Ottieni l'immagine di output
        output_image = output.squeeze().cpu().numpy().transpose(1, 2, 0)
        output_image = (output_image * 255).clip(0, 255).astype(np.uint8)

        # Converti l'immagine in formato PIL
        output_image = Image.fromarray(output_image)

        # Salva l'immagine in un buffer in memoria
        output_buffer = io.BytesIO()
        output_image.save(output_buffer, format="JPEG")
        
        # Ritorna i dati binari dell'immagine
        return output_buffer.getvalue()
