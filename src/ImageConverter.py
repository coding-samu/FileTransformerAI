import torch
from PIL import Image
from torchvision import transforms
import cv2
import numpy as np
from model_architecture import RRDBNet

class better_image:
    def __init__(self):
        # Inizializza il modello ESRGAN (RRDBNet)
        self.model = RRDBNet(in_nc=3, out_nc=3, nf=64, nb=23)
        self.model.load_state_dict(torch.load('models/RealESRGAN_x4plus.pth'))
        self.model.eval()

    def convert(self, input_image_path):
        # Carica e pre-processa l'immagine
        image = cv2.imread(input_image_path, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = transforms.ToTensor()(image).unsqueeze(0)

        # Inference
        with torch.no_grad():
            output_image = self.model(image)
        output_image = output_image.squeeze(0).cpu().numpy()

        # Post-processa l'immagine
        output_image = np.transpose(output_image, (1, 2, 0))
        output_image = (output_image * 255.0).clip(0, 255).astype(np.uint8)
        output_image = Image.fromarray(output_image)
        return output_image