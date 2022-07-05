import requests

API_KEY = "ef8f14ae707e45b3606b64fc95dbfc50"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    # print(weather)
    temperature = round(data["main"]["temp"] - 273.15, 2)
    # print(temperature)
    print("Weather: ", weather)
    print("Temperature: ", temperature, "celsius")
    # print(data)
else:
    print("An error occurred, for example the API key could be expired")

