import torch
from PIL import Image
from torchvision import transforms

from model.model import create_model


class SkinModel:

    def __init__(self):

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        # Create model
        self.model = create_model(
            num_classes=2
        )

        # Evaluation mode
        self.model.eval()

        # Move model to CPU/GPU
        self.model.to(self.device)

        # Image preprocessing
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[
                    0.485,
                    0.456,
                    0.406
                ],
                std=[
                    0.229,
                    0.224,
                    0.225
                ]
            )
        ])

    def predict(self, image_path):

        # Open image
        image = Image.open(
            image_path
        ).convert("RGB")

        # Preprocess
        image = self.transform(
            image
        )

        # Add batch dimension
        image = image.unsqueeze(0)

        # Move to device
        image = image.to(
            self.device
        )

        # Model prediction
        with torch.no_grad():

            outputs = self.model(
                image
            )

            probabilities = torch.softmax(
                outputs,
                dim=1
            )

            confidence, predicted_class = torch.max(
                probabilities,
                dim=1
            )

        prediction = predicted_class.item()

        confidence = confidence.item()

        return prediction, confidence