import os
import sys

# Get the main skintumour project folder
project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# Add project root to Python's import path
sys.path.insert(0, project_root)

from model.inference import SkinModel


# Image to test
image_path = os.path.join(
    project_root,
    "mobile",
    "captured_skin.jpg"
)

print("Testing image:")
print(image_path)


# Check image exists
if not os.path.exists(image_path):
    print("ERROR: captured_skin.jpg not found.")
    exit()


# Load model
print("Loading model...")

model = SkinModel()

print("Running prediction...")

prediction, confidence = model.predict(
    image_path
)

print()
print("Prediction:", prediction)
print("Confidence:", confidence)