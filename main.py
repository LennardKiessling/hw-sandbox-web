import requests
import os
import time
import shutil

# Controlladresses A
ip_address_usb_switch_Analyse_TOGGLE = "http://192.168.1.227/cm?cmnd=Power%20TOGGLE"
ip_address_usb_switch_Analyse_ON = "http://192.168.1.227/cm?cmnd=Power%20ON"
ip_address_usb_switch_Analyse_OFF = "http://192.168.1.227/cm?cmnd=Power%20off"

# Controlladresses B
ip_address_usb_switch_Sandbox_TOGGLE = "http://192.168.1.128/cm?cmnd=Power%20TOGGLE"
ip_address_usb_switch_Sandbox_ON = "http://192.168.1.128/cm?cmnd=Power%20ON"
ip_address_usb_switch_Sandbox_OFF = "http://192.168.1.128/cm?cmnd=Power%20off"

# Malware dir
directory = "C:/Users/Lennard/malware"


# USB A
def USB_Analyse_ON():
    try:
        response = requests.get(ip_address_usb_switch_Analyse_ON)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred with USB switch A: {e}")


def USB_Analyse_OFF():
    try:
        response = requests.get(ip_address_usb_switch_Analyse_OFF)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred with USB switch A: {e}")


def USB_Analyse_Toggle():
    try:
        response = requests.get(ip_address_usb_switch_Analyse_TOGGLE)
        response.raise_for_status()
        if response.status_code == 200:
            print(response.text)
            return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred with USB switch A: {e}")


# USB B
def USB_Sandbox_ON():
    try:
        response = requests.get(ip_address_usb_switch_Sandbox_ON)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred with USB switch A: {e}")


def USB_Sandbox_OFF():
    try:
        response = requests.get(ip_address_usb_switch_Sandbox_OFF)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred with USB switch A: {e}")


def USB_Sandbox_Toggle():
    try:
        response = requests.get(ip_address_usb_switch_Sandbox_TOGGLE)
        response.raise_for_status()
        if response.status_code == 200:
            return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred with USB switch A: {e}")


while True:
    files = os.listdir(directory)

    # Filtern, um nur Dateien zu erhalten
    files = [f for f in files if os.path.isfile(os.path.join(directory, f))]

    if files:
        print(f"Es gibt Dateien in {directory}.")


        # Switch zeigt auf Analyse
        USB_Analyse_ON()
        USB_Sandbox_OFF()

        source = f"C:/Users/Lennard/malware/{files[0]}"

        # Externe SSD
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


        # Switch zeigt auf Sandbox
        USB_Analyse_Toggle()
        USB_Sandbox_Toggle()

        time.sleep(12000)


        # Sandbox auch aus
        USB_Sandbox_OFF()

        time.sleep(6000)

        USB_Sandbox_Toggle()

        time.sleep(1000)

        USB_Sandbox_Toggle()

    else:
        print(f"Es gibt keine Dateien in {directory}.")
        # Pro Minute ein Check ob neue Datei
        time.sleep(60)
