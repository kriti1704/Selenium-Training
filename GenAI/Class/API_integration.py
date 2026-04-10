import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the API key from the environment variable
API_KEY = os.environ.get('API_KEY')


url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent" 

headers = {
    "x-goog-api-key": API_KEY,
    "Content-Type": "application/json"
}

payload = {
    "contents": [
      {
        "parts": [
          {
            "text": "Explain the concept of machine learning in simple terms."
          }
        ]
      }
    ]
  }

response = requests.post(url, headers=headers, json=payload)
print("Status Code:", response.status_code)
data = response.json()
print("Response Data:", data)

if "candidates" in data:
    print("Generated Text:", data["candidates"][0]["content"]["parts"][0]["text"])
else:
    print("Error:",data)
