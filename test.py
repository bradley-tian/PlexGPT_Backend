import requests
import json

prompt = "What is PlexTech at Berkeley?"
print(requests.get(f'http://127.0.0.1:5000/text_completion/{prompt}').json())