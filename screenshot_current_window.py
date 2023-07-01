from subprocess import run

def get_focused_window():
    return run(['xdotool', 'getwindowfocus', 'getwindowpid', 'getwindowname'], capture_output=True).stdout.decode('utf-8').split()
