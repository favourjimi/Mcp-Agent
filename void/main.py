from datetime import datetime
import subprocess

# VOID v0.1

name = input("What should I call you? ")

print("\n==============================")
print("       VOID v0.1")
print("==============================")
print(f"Hello, {name}! I am Void.")
print("Your personal assistant is starting...")
print("Type 'help' to see my commands.")

while True:
    command = input(f"\n{name} > ").strip().lower()

    if command == "open notepad":
        print("Void: Opening Notepad...")

        try:
            subprocess.Popen(["notepad.exe"])
            print("Void: Notepad opened successfully!")

        except OSError as error:
            print(f"Void: I couldn't open Notepad. {error}")

    elif command == "hello":
    #if command == "hello":
        print(f"Void: Hello, {name}!")

    elif command == "status":
        print("Void: I am online and running.")

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
""")

    elif command == "exit":
        print(f"Void: Goodbye, {name}. See you soon!")
        break

    else:
        print("Void: I don't know that command yet.")
        print("Type 'help' to see what I can do.")
