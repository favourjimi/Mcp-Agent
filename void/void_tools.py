import subprocess


# Approved applications Void can launch
APPLICATIONS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe"
}


def open_application(app_name):
    """Open an approved Windows application."""

    app_name = app_name.lower().strip()

    if app_name not in APPLICATIONS:
        return f"I don't know how to open {app_name} yet."

    try:
        subprocess.Popen([APPLICATIONS[app_name]])
        return f"Opening {app_name}."

    except OSError as error:
        return f"I couldn't open {app_name}: {error}"


def get_available_applications():
    """Return the applications Void is allowed to open."""
    return list(APPLICATIONS.keys())


# VOID TOOL REGISTRY
TOOLS = {
    "open_application": open_application,
    "launch_application": open_application,
    "start_application": open_application,
    "please_open_application": open_application,
    "get_available_applications": get_available_applications
}