import tkinter as tk
import requests
print(requests.__version__)

# Replace with your OpenWeatherMap API key
API_KEY = "f847427b712453948734fd69edd73054"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Map weather keywords to icons
WEATHER_ICONS = {
    "clear": "☀️",
    "clouds": "☁️",
    "rain": "🌧️",
    "drizzle": "🌦️",
    "thunderstorm": "⛈️",
    "snow": "❄️",
    "mist": "🌫️",
    "fog": "🌫️",
    "haze": "🌫️"
}

def get_weather():
    city = city_entry.get().strip()
    if not city:
        result_label.config(text="Please enter a city name.")
        return
    
    url = f"{BASE_URL}q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        result_label.config(text=f"Error fetching data: {e}")
        return

    if data.get("cod") != "404":
        main = data["main"]
        weather = data["weather"][0]
        temp = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        description = weather["description"].capitalize()

        # Pick an icon based on the weather condition
        icon = ""
        for key, symbol in WEATHER_ICONS.items():
            if key in weather["description"].lower():
                icon = symbol
                break

        result_label.config(
            text=f"City: {city}\n"
                 f"Temperature: {temp} \u00B0C\n"
                 f"Pressure: {pressure} hPa\n"
                 f"Humidity: {humidity}%\n"
                 f"Condition: {description} {icon}"
        )
    else:
        result_label.config(text="City not found.")

# Tkinter UI
root = tk.Tk()
root.title("Weather App")
root.geometry("350x300")

tk.Label(root, text="Enter City:", font=("Arial", 12)).pack(pady=5)
city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather, font=("Arial", 12)).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()

