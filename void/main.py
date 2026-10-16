from void_tools import open_application
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
# =========================
# VOID TOOLS
# =========================

# def open_application(app_name):
 #    """Open an approved Windows application."""

  #  applications = {
   #     "notepad": "notepad.exe",
    #    "calculator": "calc.exe",
     #   "paint": "mspaint.exe"
    #}

    #app_name = app_name.lower().strip()

    #if app_name not in applications:
     #   return f"I don't know how to open {app_name} yet."

    #try:
     #   subprocess.Popen([applications[app_name]])
      #  return f"Opening {app_name}."

    #except OSError as error:
    #    return f"I couldn't open {app_name}: {error}"

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

   # if command == "open notepad":
    #    print("Void: Opening Notepad...")

     #   try:
      #      subprocess.Popen(["notepad.exe"])
       #     print("Void: Notepad opened successfully!")

        #except OSError as error:
         #   print(f"Void: I couldn't open Notepad. {error}")

    if command.startswith("open "):
        app_name = command[len("open "):].strip()
        result = open_application(app_name)
        print(f"Void: {result}")

    elif command.startswith("launch "):
        app_name = command[len("launch "):].strip()
        result = open_application(app_name)
        print(f"Void: {result}")

    elif command.startswith("start "):
        app_name = command[len("start "):].strip()
        result = open_application(app_name)
        print(f"Void: {result}")

    elif command.startswith("please open "):
        app_name = command[len("please open "):].strip()
        result = open_application(app_name)
        print(f"Void: {result}")


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
remember <fact> - Save something to memory
what is/are <topic>? - Ask Void about a saved fact
""")
    elif command.startswith("remember "):
        fact = command[len("remember "):].strip()

        if fact:
            memory.setdefault("facts", [])
            memory["facts"].append(fact)
            save_memory(memory)

            print(f"Void: I'll remember that {fact}.")
        else:
            print("Void: Tell me what you want me to remember.")

    elif command.startswith(("what is ", "what are ")):
        question_prefix = "what are " if command.startswith("what are ") else "what is "
        question = command[len(question_prefix):].rstrip("?.!").strip()

        facts = memory.get("facts", [])
        matching_facts = [
            fact for fact in facts
            if question in fact or fact.startswith(question)
        ]

        if matching_facts:
            print(f"Void: I remember that you said {matching_facts[-1]}.")
        else:
            print("Void: I don't remember that yet.")
    elif command == "exit":
        print(f"Void: Goodbye, {name}. See you soon!")
        break

    else:
        print("Void: I don't know that command yet.")
        print("Type 'help' to see what I can do.")
