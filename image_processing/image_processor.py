import cv2
import numpy as np
from PIL import Image


def process_image(image_path, output_path="processed_skin.jpg"):

    # Read image using OpenCV
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Could not read the image.")

    print("Original image shape:", image.shape)

    # Convert BGR → RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert OpenCV image to Pillow image
    image = Image.fromarray(image)

    # Resize image
    image = image.resize((224, 224))

    # Convert back to NumPy array
    image = np.array(image)

    # Normalize pixel values
    image = image.astype(np.float32) / 255.0

    # Convert back to 0-255 for saving
    processed = (image * 255).astype(np.uint8)

    # RGB → BGR for OpenCV
    processed = cv2.cvtColor(
        processed,
        cv2.COLOR_RGB2BGR
    )

    # Save processed image
    cv2.imwrite(
        output_path,
        processed
    )

    print("Processed image shape:", processed.shape)
    print("Processed image saved:", output_path)

    return processed


if __name__ == "__main__":

    process_image(
        "../mobile/captured_skin.jpg"
    )