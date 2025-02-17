import requests

api_url = "http://127.0.0.1:5000/api/appointments"
response = requests.get(api_url)

try:
    data = response.json()
    print("🔍 API Response:\n", data)
except Exception as e:
    print(f"❌ Error parsing API response: {e}")
