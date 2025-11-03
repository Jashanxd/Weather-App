import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get().strip()
    api_key = "507ca6c72b85394cdeaf6309c77f7c41"
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name!")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            result_label.config(text=f"City not found: {city}", fg="#ff4d4d")
            return

        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        result_label.config(
            text=f"🌤 Weather: {weather}\n🌡 Temperature: {temp}°C",
            fg="#ffffff"
        )
    except Exception as e:
        result_label.config(text=f"Error: {e}", fg="#ff4d4d")

root = tk.Tk()
root.title("Weather App 🌦️")

window_width = 600
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = int((screen_width / 2) - (window_width / 2))
y_position = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
root.resizable(False, False)
root.configure(bg="#1e1e2f")

header = tk.Label(
    root,
    text="🌍 Simple Weather App",
    font=("Helvetica", 22, "bold"),
    fg="#00ffcc",
    bg="#1e1e2f",
)
header.pack(pady=30)

entry_frame = tk.Frame(root, bg="#1e1e2f")
entry_frame.pack(pady=15)

city_label = tk.Label(
    entry_frame,
    text="Enter City Name:",
    font=("Helvetica", 14),
    fg="#ffffff",
    bg="#1e1e2f",
)
city_label.pack()

city_entry = tk.Entry(
    entry_frame,
    font=("Helvetica", 16),
    width=25,
    justify="center",
    relief="flat",
    bg="#2b2b3d",
    fg="#ffffff",
    insertbackground="white",
)
city_entry.pack(padx=10, pady=10)

def on_hover(e):
    get_button.config(bg="#00ffcc", fg="#1e1e2f")

def on_leave(e):
    get_button.config(bg="#009999", fg="#ffffff")

get_button = tk.Button(
    root,
    text="Get Weather",
    font=("Helvetica", 14, "bold"),
    bg="#009999",
    fg="#ffffff",
    relief="flat",
    padx=20,
    pady=10,
    activebackground="#00ffcc",
    activeforeground="#1e1e2f",
    command=get_weather,
)
get_button.bind("<Enter>", on_hover)
get_button.bind("<Leave>", on_leave)
get_button.pack(pady=25)

result_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 16),
    bg="#1e1e2f",
    fg="#ffffff",
    justify="center",
)
result_label.pack(pady=40)

root.mainloop()
