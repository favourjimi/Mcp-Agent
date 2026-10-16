from datetime import datetime
#import sys
#print(sys.executable)
import subprocess
import platform
import json
import os
import psutil

# VOID v0.1

#name = input("What should I call you? ") old line in first part
# VOID MEMORY SYSTEM

MEMORY_FILE = "void_memory.json"


def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return {}

    return {}


def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, indent=4)


# Load previously saved information
memory = load_memory()

if memory.get("name"):
    name = memory["name"]
    print(f"Void: Welcome back, {name}!")
else:
    name = input("What should I call you? ").strip()

    if not name:
        name = "User"

    memory["name"] = name
    save_memory(memory)
    print(f"Void: Nice to meet you, {name}!")

print("\n==============================")
print("       VOID v0.1")
print("==============================")
print(f"Hello, {name}! I am Void.")
print("Your personal assistant is starting...")
print("Type 'help' to see my commands.")

while True:
    command = input(f"\n{name} > ").strip().lower()

    # Understand different ways of requesting the same action
    command = command.replace("launch ", "open ")
    command = command.replace("start ", "open ")
    command = command.replace("please open ", "open ")

    if command == "open notepad":
        print("Void: Opening Notepad...")

        try:
            subprocess.Popen(["notepad.exe"])
            print("Void: Notepad opened successfully!")

        except OSError as error:
            print(f"Void: I couldn't open Notepad. {error}")

    elif command == "system":
        system_name = platform.system()
        system_version = platform.version()

        print(f"Void: You are running {system_name}.")
        print(f"Void: System version: {system_version}")

    elif command == "memory":
        ram = psutil.virtual_memory()

        total_ram = ram.total / (1024 ** 3)
        used_ram = ram.used / (1024 ** 3)
        available_ram = ram.available / (1024 ** 3)

        print(f"Void: Total RAM: {total_ram:.2f} GB")
        print(f"Void: Used RAM: {used_ram:.2f} GB")
        print(f"Void: Available RAM: {available_ram:.2f} GB")
        print(f"Void: RAM usage: {ram.percent}%")

    elif command == "cpu":
        cpu_usage = psutil.cpu_percent(interval=1)

        print(f"Void: CPU usage: {cpu_usage}%")

    elif command == "battery":
        battery = psutil.sensors_battery()

        if battery is None:
            print("Void: I couldn't detect a battery.")
            print("Void: Your computer may be a desktop.")

        else:
            print(f"Void: Battery level: {battery.percent}%")

            if battery.power_plugged:
                print("Void: Your computer is plugged in.")
            else:
                print("Void: Your computer is running on battery.")

    elif command == "hello":
    #if command == "hello": old part
        print(f"Void: Hello, {name}!")

    elif command == "status":
        print("Void: I am online and running.")

    elif command == "remember":
        if memory:
            print("Void: Here is what I remember:")

            for key, value in memory.items():
                print(f"- {key}: {value}")
        else:
            print("Void: My memory is currently empty.")

    elif command == "time":
        current_time = datetime.now().strftime("%I:%M:%S %p")
        print(f"Void: The current time is {current_time}.")

    elif command == "date":
        current_date = datetime.now().strftime("%B %d, %Y")
        print(f"Void: Today is {current_date}.")

    elif command == "help":
        print("""
VOID COMMANDS
-------------
hello  - Say hello to Void
status - Check Void's status
time   - Get the current time
date   - Get today's date
help   - Show available commands
exit   - Shut down Void
system      - Check operating system information
memory      - Check RAM usage
cpu         - Check processor usage
battery     - Check battery status
open notepad     - Open Notepad
launch notepad   - Launch Notepad
start notepad    - Start Notepad
open calculator  - Open Calculator
launch calculator - Launch Calculator
open paint       - Open Paint
launch paint     - Launch Paint
""")

    elif command == "exit":
        print(f"Void: Goodbye, {name}. See you soon!")
        break

    else:
        print("Void: I don't know that command yet.")
        print("Type 'help' to see what I can do.")
