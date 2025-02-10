import requests
import time

time.sleep(5)
response = requests.get("http://server:5000/")
print("Resposta do servidor:", response.text)