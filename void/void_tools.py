import subprocess


def open_application(app_name):
    """Open an approved Windows application."""

    applications = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe"
    }

    app_name = app_name.lower().strip()

    if app_name not in applications:
        return f"I don't know how to open {app_name} yet."

    try:
        subprocess.Popen([applications[app_name]])
        return f"Opening {app_name}."

    except OSError as error:
        return f"I couldn't open {app_name}: {error}"