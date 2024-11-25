import tkinter as tk
from tkinter import ttk
import requests
import threading



cities = [
    "Oslo", "Bergen", "Trondheim", "Stavanger", "Tromsø",
    "Kristiansand", "Ålesund", "Bodø", "Sandefjord", "Drammen",
    "Narvik", "Lillehammer", "Fredrikstad", "Hamar", "Harstad",
    "Alta", "Molde", "Arendal", "Gjøvik", "Haugesund"
]

def get_weather(city):
    url = f"https://wttr.in/{city}?format=%C+%t"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Error: {e}"

def fetch_weather():
    for i, city in enumerate(cities):
        weather_info = get_weather(city)
        labels[i].config(text=f"{city}: {weather_info}")

    loading_label.pack_forget()
    refresh_button.config(state="normal")

def update_weather():
    refresh_button.config(state="disabled")
    loading_label.pack(pady=10)
    threading.Thread(target=fetch_weather).start()


root = tk.Tk()
root.title("Norwegian Weather")
root.geometry("500x760")
root.resizable(False, False)


header = tk.Label(root, text="Current Weather in Norwegian Cities", font=("Arial", 16, "bold"))
header.pack(pady=10)


loading_label = tk.Label(root, text="Loading weather data, please wait...", font=("Arial", 12), fg="blue")


weather_frame = ttk.Frame(root)
weather_frame.pack(pady=10)


labels = []
for city in cities:
    label = tk.Label(weather_frame, text=f"{city}: Waiting...", font=("Arial", 12))
    label.pack(anchor="w", padx=10, pady=2)
    labels.append(label)


refresh_button = ttk.Button(root, text="Refresh Weather", command=update_weather)
refresh_button.pack(pady=10)


update_weather()
root.mainloop()
