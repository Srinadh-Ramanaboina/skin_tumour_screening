import os
import sys


# Get the skintumour project root
project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# Add project root to Python path
sys.path.insert(0, project_root)


from mobile.result_handler import ResultHandler


# Test response from Flask
response = {
    "prediction": 0,
    "confidence": 0.5796157717704773
}


# Process response
result = ResultHandler.process(
    response
)


print("Result:")
print(result)