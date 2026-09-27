import requests


url = "http://127.0.0.1:5000/predict"


response = requests.post(
    url
)


print("Status Code:")
print(response.status_code)

print()

print("Response:")
print(response.json())