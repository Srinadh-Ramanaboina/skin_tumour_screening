import os
from PIL import Image


class ImageValidator:

    ALLOWED_FORMATS = {
        "JPEG",
        "PNG"
    }

    MIN_WIDTH = 224
    MIN_HEIGHT = 224

    @staticmethod
    def validate(image_path):

        # Check whether file exists
        if not os.path.exists(image_path):
            return {
                "valid": False,
                "message": "Image file does not exist."
            }

        # Check whether file is empty
        if os.path.getsize(image_path) == 0:
            return {
                "valid": False,
                "message": "Image file is empty."
            }

        # Try opening the image
        try:
            image = Image.open(image_path)

            # Verify image integrity
            image.verify()

        except Exception:
            return {
                "valid": False,
                "message": "Image is corrupted or invalid."
            }

        # Open again because verify() closes the image
        try:
            image = Image.open(image_path)

            image_format = image.format
            width, height = image.size

        except Exception:
            return {
                "valid": False,
                "message": "Unable to read image information."
            }

        # Check format
        if image_format not in ImageValidator.ALLOWED_FORMATS:
            return {
                "valid": False,
                "message": (
                    f"Unsupported image format: "
                    f"{image_format}"
                )
            }

        # Check dimensions
        if (
            width < ImageValidator.MIN_WIDTH
            or height < ImageValidator.MIN_HEIGHT
        ):
            return {
                "valid": False,
                "message": (
                    "Image resolution is too small. "
                    "Minimum resolution is 224x224."
                )
            }

        return {
            "valid": True,
            "message": "Image is valid.",
            "format": image_format,
            "width": width,
            "height": height
        }