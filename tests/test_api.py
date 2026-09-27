import os
import requests


# Find the main project folder
project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# Build the image path
image_path = os.path.join(
    project_root,
    "mobile",
    "captured_skin.jpg"
)

print("Looking for image at:")
print(image_path)


# Check whether image exists
if not os.path.exists(image_path):
    print("ERROR: captured_skin.jpg was not found.")
    print("Please capture an image using the Kivy camera first.")
    exit()


# Flask API
url = "http://127.0.0.1:5000/predict"


# Send image
with open(image_path, "rb") as image:

    files = {
        "image": (
            "captured_skin.jpg",
            image,
            "image/jpeg"
        )
    }

    response = requests.post(
        url,
        files=files
    )


print("Status Code:", response.status_code)

print("Response:")
print(response.json())