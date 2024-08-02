import requests
import tkinter as tk
from tkinter import messagebox


# Function to fetch weather data
def get_weather():
    api_key = '80e901d8d88e4f1984f40b0a33cb1d36'
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data['cod'] != 200:
            raise Exception(data['message'])

        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        result = f"Temperature: {temperature}°C\nDescription: {weather_description.capitalize()}"

    except Exception as e:
        result = f"Error: {str(e)}"

    result_label.config(text=result)


# Set up the GUI
root = tk.Tk()
root.title("Weather App")

# Create and place widgets
city_label = tk.Label(root, text="Enter city:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_button = tk.Button(root, text="Get Weather", command=get_weather)
get_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()