import requests
import os
import time
import shutil


ip_address_usb_switch_A = "http://192.168.1.227/cm?cmnd=Power%20TOGGLE"
ip_address_usb_switch_B = "http://192.168.1.128/cm?cmnd=Power%20TOGGLE"
directory = "C:/Users/Lennard/malware"

while True:
    files = os.listdir(directory)

    # Filtern, um nur Dateien zu erhalten
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]

    if files:
        print(f"Es gibt Dateien in {directory}.")

        try:
            response = requests.get(ip_address_usb_switch_A)
            response.raise_for_status()
            print(f"Status Code A: {response.status_code}")
            print(f"Response Text A: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred with USB switch A: {e}")

        try:
            response = requests.get(ip_address_usb_switch_B)
            response.raise_for_status()
            print(f"Status Code B: {response.status_code}")
            print(f"Response Text B: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred with USB switch B: {e}")

        source = f"C:/Users/Lennard/malware/{files[0]}"

        # Quelle und Ziel definieren
        destination_directory = "C:/Users/Lennard/malware1/"

        destination = os.path.join(destination_directory, os.path.basename(source))

        try:
            shutil.move(source, destination)
            print(f"Datei wurde nach {destination} verschoben.")
        except FileNotFoundError as e:
            print(f"Fehler: Die Datei oder das Verzeichnis wurde nicht gefunden. ({e})")
        except PermissionError as e:
            print(f"Fehler: Berechtigung verweigert. ({e})")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

    else:
        print(f"Es gibt keine Dateien in {directory}.")
        time.sleep(60)
