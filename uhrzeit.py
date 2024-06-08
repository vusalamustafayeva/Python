

# Dieses Programm zeigt die aktuelle Uhrzeit und Wetterinformationen für bestimmte Städte an.
# Eine grafische Benutzeroberfläche (GUI) wird mit der Tkinter-Bibliothek erstellt.
# Wetterdaten werden über die OpenWeatherMap API abgerufen.

import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz
import requests

# Wörterbuch mit Zeitzonen und Koordinaten der gewünschten Städte
staedte = {
    'San Francisco': ('America/Los_Angeles', 37.7749, -122.4194),
    'New York': ('America/New_York', 40.7128, -74.0060),
    'Ottawa': ('America/Toronto', 45.4215, -75.6972),
    'St. Helena': ('Atlantic/St_Helena', -15.9650, -5.7089),
    'Kapstadt': ('Africa/Johannesburg', -33.9249, 18.4241),
    'Berlin': ('Europe/Berlin', 52.5200, 13.4050),
    'Warschau': ('Europe/Warsaw', 52.2297, 21.0122),
    'Moskau': ('Europe/Moscow', 55.7558, 37.6173),
    'Kalkutta': ('Asia/Kolkata', 22.5726, 88.3639),
    'Peking': ('Asia/Shanghai', 39.9042, 116.4074),
    'Tokio': ('Asia/Tokyo', 35.6895, 139.6917)
}

# API-Schlüssel für OpenWeatherMap (Fügen Sie Ihren eigenen API-Schlüssel hier ein)
API_SCHLUESSEL = 'YOUR_API_KEY_HERE'

# Nachrichten, die den Wetterbeschreibungen entsprechen
wetter_nachrichten = {
    'clear sky': 'Heute ist es klar. Ein schöner Tag!',
    'few clouds': 'Ein paar Wolken. Genießen Sie den Tag!',
    'scattered clouds': 'Vereinzelte Wolken. Es könnte ein kühler Tag sein.',
    'broken clouds': 'Aufgelockerte Bewölkung. Überprüfen Sie das Wetter, bevor Sie hinausgehen.',
    'shower rain': 'Schauer. Vergessen Sie nicht Ihren Regenschirm!',
    'rain': 'Regnerisch. Nehmen Sie eine Regenjacke mit!',
    'thunderstorm': 'Gewitter. Bleiben Sie möglichst zu Hause!',
    'snow': 'Schnee! Ziehen Sie sich warm an und seien Sie vorsichtig.',
    'mist': 'Nebelig. Fahren Sie vorsichtig und passen Sie draußen gut auf.'
}

def get_zeit_in_stadt(stadt_name):
    """
    Gibt die aktuelle Uhrzeit für die angegebene Stadt zurück.
    
    Args:
        stadt_name (str): Name der Stadt.
    
    Returns:
        str: Die lokale Uhrzeit der Stadt im Format 'YYYY-MM-DD HH:MM:SS'.
    """
    zeitzone, _, _ = staedte[stadt_name]
    stadt_zeitzone = pytz.timezone(zeitzone)
    stadt_zeit = datetime.now(stadt_zeitzone)
    return stadt_zeit.strftime('%Y-%m-%d %H:%M:%S')

def get_wetter_in_stadt(stadt_name):
    """
    Gibt die Wetterinformationen für die angegebene Stadt zurück.
    
    Args:
        stadt_name (str): Name der Stadt.
    
    Returns:
        str: Wetterbeschreibung, Temperatur und entsprechende Nachricht.
    """
    _, lat, lon = staedte[stadt_name]
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_SCHLUESSEL}&units=metric'
    response = requests.get(url)
    wetter_daten = response.json()
    
    if response.status_code == 200:
        beschreibung = wetter_daten['weather'][0]['description']
        temperatur = wetter_daten['main']['temp']
        wetter_msg = wetter_nachrichten.get(beschreibung, 'Wetterdaten nicht verfügbar.')
        return f"{beschreibung.capitalize()}, {temperatur}°C\n{wetter_msg}"
    else:
        return "Wetterdaten nicht verfügbar"

def show_info():
    """
    Zeigt die Uhrzeit und Wetterinformationen für die ausgewählte Stadt auf der GUI an.
    """
    ausgewaehlte_stadt = stadt_var.get()
    if ausgewaehlte_stadt:
        zeit_str = get_zeit_in_stadt(ausgewaehlte_stadt)
        wetter_str = get_wetter_in_stadt(ausgewaehlte_stadt)
        result_label.config(text=f"Aktuelle Uhrzeit in {ausgewaehlte_stadt}: {zeit_str}\nWetter: {wetter_str}")
    else:
        result_label.config(text="Bitte wählen Sie eine Stadt aus.")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Aktuelle Uhrzeit und Wetter in Städten")

# Dropdown-Menü für die Stadtauswahl
stadt_var = tk.StringVar()
stadt_label = ttk.Label(root, text="Wählen Sie eine Stadt aus:")
stadt_label.pack(pady=10)

stadt_dropdown = ttk.Combobox(root, textvariable=stadt_var, values=list(staedte.keys()))
stadt_dropdown.pack(pady=10)

# Schaltfläche zum Anzeigen der Informationen
show_info_button = ttk.Button(root, text="Informationen anzeigen", command=show_info)
show_info_button.pack(pady=10)

# Etikett zum Anzeigen der Ergebnisse
result_label = ttk.Label(root, text="")
result_label.pack(pady=20)

# Hauptschleife starten
root.mainloop()