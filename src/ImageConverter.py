from PIL import Image
import torch
from torchvision import transforms
from model_architecture import ImageModel

class better_image:
    def __init__(self):
        # Carica un modello pre-addestrato (ad esempio, un modello di super risoluzione)
        self.model = ImageModel()
        self.model.load_state_dict(torch.load('models/trained_model.pth'))
        self.model.eval()
        self.transform = transforms.Compose([
            transforms.Resize((256, 256)),
            transforms.ToTensor(),
        ])

    def convert(self, input_image_path):
        image = Image.open(input_image_path)
        image = self.transform(image).unsqueeze(0)
        with torch.no_grad():
            output_image = self.model(image)
        output_image = transforms.ToPILImage()(output_image.squeeze(0))
        return output_image
