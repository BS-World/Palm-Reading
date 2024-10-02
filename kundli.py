import tkinter as tk
from astropy.time import Time
import ephem
import matplotlib.pyplot as plt
from datetime import datetime
import re
from geopy.geocoders import Nominatim
import os

# Initialize geolocator
geolocator = Nominatim(user_agent="kundli_app")

# Function to retrieve latitude and longitude based on place name
def get_lat_lon(place_of_birth):
    location = geolocator.geocode(place_of_birth)
    if location:
        return str(location.latitude), str(location.longitude)
    else:
        raise ValueError("Place not found.")

# Read interpretations from a file
def read_interpretations(file_path):
    interpretations = {}
    with open(file_path, 'r') as file:
        for line in file:
            planet, description = line.strip().split(':', 1)
            interpretations[planet.strip()] = description.strip()
    return interpretations

# Validate user input
def validate_input(dob, tob):
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', dob):
        return False, "Invalid date format. Use YYYY-MM-DD."
    try:
        datetime.strptime(dob, '%Y-%m-%d')
    except ValueError:
        return False, "Invalid date. Please check the values."
    
    if not re.match(r'^\d{2}:\d{2}$', tob):
        return False, "Invalid time format. Use HH:MM."
    try:
        datetime.strptime(tob, '%H:%M')
    except ValueError:
        return False, "Invalid time. Please check the values."
    
    return True, ""

# Save Kundli to a file
def save_kundli(planet_positions, file_path):
    with open(file_path, 'w') as file:
        file.write("Bharat Kundli Chart\n")
        file.write("-------------------\n")
        for planet, position in planet_positions.items():
            file.write(f"{planet}: Altitude={position[0]:.2f} degrees, Azimuth={position[1]:.2f} degrees\n")
    print(f"Kundli saved to {file_path}")

def submit_details():
    date_of_birth = dob_entry.get()
    time_of_birth = tob_entry.get()
    place_of_birth = pob_entry.get()

    is_valid, message = validate_input(date_of_birth, time_of_birth)
    if not is_valid:
        tk.messagebox.showerror("Input Error", message)
        return

    try:
        positions = calculate_kundli(date_of_birth, time_of_birth, place_of_birth)
        display_kundli(positions)
    except ValueError as ve:
        tk.messagebox.showerror("Error", str(ve))

def calculate_kundli(date_of_birth, time_of_birth, place_of_birth):
    datetime_str = f"{date_of_birth} {time_of_birth}"
    time = Time(datetime_str)

    observer = ephem.Observer()
    observer.lat, observer.lon = get_lat_lon(place_of_birth)
    observer.date = time.jd

    # Calculate positions for all major planets
    planets = {
        'Sun': ephem.Sun(observer),
        'Moon': ephem.Moon(observer),
        'Mercury': ephem.Mercury(observer),
        'Venus': ephem.Venus(observer),
        'Mars': ephem.Mars(observer),
        'Jupiter': ephem.Jupiter(observer),
        'Saturn': ephem.Saturn(observer),
        'Uranus': ephem.Uranus(observer),
        'Neptune': ephem.Neptune(observer),
        'Pluto': ephem.Pluto(observer)
    }

    positions = {planet: (body.alt, body.az) for planet, body in planets.items()}
    return positions

def display_kundli(planet_positions):
    planet_names = list(planet_positions.keys())
    altitudes = [pos[0] for pos in planet_positions.values()]

    plt.figure(figsize=(10, 6))
    plt.bar(planet_names, altitudes, color='skyblue')
    plt.title('Bharat Kundli Chart')
    plt.xlabel('Planets')
    plt.ylabel('Altitude (degrees)')
    
    for i, (planet, position) in enumerate(planet_positions.items()):
        plt.text(i, position[0] + 0.5, f"{position[0]:.2f}", ha='center')

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid()
    plt.show()

    # Read interpretations from an external file
    interpretations = read_interpretations('interpretations.txt')
    interpretation_text = "\n".join([f"{planet}: {interpretations[planet]}" for planet in planet_names])
    
    # Save Kundli to a file
    save_kundli(planet_positions, "kundli.txt")
    
    # Display interpretations
    tk.messagebox.showinfo("Astrological Interpretations", interpretation_text)

# Create GUI
root = tk.Tk()
root.title("Bharat Kundli Application")

tk.Label(root, text="Date of Birth (YYYY-MM-DD):").pack()
dob_entry = tk.Entry(root)
dob_entry.pack()

tk.Label(root, text="Time of Birth (HH:MM):").pack()
tob_entry = tk.Entry(root)
tob_entry.pack()

tk.Label(root, text="Place of Birth:").pack()
pob_entry = tk.Entry(root)
pob_entry.pack()

tk.Button(root, text="Submit", command=submit_details).pack()

root.mainloop()
