import torch
import torch.nn as nn
from torchvision import models


def create_model(num_classes=2):

    model = models.resnet18(
        weights=models.ResNet18_Weights.DEFAULT
    )

    # Replace the final classification layer
    input_features = model.fc.in_features

    model.fc = nn.Linear(
        input_features,
        num_classes
    )

    return model


if __name__ == "__main__":

    model = create_model()

    print(model)