import requests

with open("sample.png", "rb") as f:
    img_bytes = f.read()


headers = {"content-type": "image/png"}
json_response = requests.post(f'http://localhost:5000/predict', data=img_bytes, headers=headers)
print(json_response)
print(json_response.text)
