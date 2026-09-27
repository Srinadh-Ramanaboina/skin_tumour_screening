import os
import sys


# Project root
project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.insert(
    0,
    project_root
)


from image_processing.image_validator import ImageValidator


image_path = os.path.join(
    project_root,
    "mobile",
    "captured_skin.jpg"
)


print("Checking image:")
print(image_path)

result = ImageValidator.validate(
    image_path
)

print()
print("Validation result:")
print(result)