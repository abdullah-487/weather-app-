import requests

API_KEY = "83ce93ce46956a246592da0b8a92a48a"
city = "lahore"

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print("City:", city)
print("Temperature:", data["main"]["temp"], "°C")
print("Weather:", data["weather"][0]["description"])
