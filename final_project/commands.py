import os
from Rayanoos import tools
from utility import echo_command, echo_result, get_confirmation
from files import get_folder_files, is_png

t = tools.SystemControls()


def exit_program():
    echo_command("Close Program")
    exit()


def mouse_move():
    echo_command("Mouse Move")

    x = int(input("X: "))
    y = int(input("Y: "))

    t.mouse_move_cursor(x, y)
    echo_result(f"Mouse moved to ({x},{y})")


def shutdown():
    echo_command("Shutdown")

    confirmed = get_confirmation(
        "Are you sure you want to shut your system down?")

    if confirmed:
        t.force_shutdown()


def standby():
    echo_command("Standby")

    confirmed = get_confirmation(
        "Are you sure you want to standby your system?")

    if confirmed:
        t.standby()


def reboot():
    echo_command("Reboot")

    confirmed = get_confirmation(
        "Are you sure you want to reboot your system?")

    if confirmed:
        t.reboot()


def kill_process():
    echo_command("Kill Process")

    process = input("Enter the process name: ")
    t.killprocess(process)

    echo_result(f"Closed '{ process }'")


def show_clipboard_content():
    echo_command("Clipboard Content")

    echo_result("Showing notification")
    t.alert("Clipboard Content", t.clipboard_get(), 2000)
    echo_result("Notification closed")


def echo_time():
    echo_command("Time")
    echo_result(t.system_time())


def echo_date():
    echo_command("Date")
    echo_result(t.system_date())


def echo_username():
    echo_command("User Name")
    echo_result(t.system_username())


def echo_path():
    echo_command("Path")
    echo_result(t.folder_windows())


def search_pic():
    echo_command("Search Picture")
    source = input("Source folder: ")
    target = input("Target folder: ")

    files = list(filter(is_png, get_folder_files(source)))
    print(files)

    # t.convert_image()


search_pic()


commands = {
    "exit": exit_program,
    "Mouse Move": mouse_move,
    "Shut Down": shutdown,
    "Standby": standby,
    "Reboot": reboot,
    "Kill process": kill_process,
    "Clipboard": show_clipboard_content,
    "Time": echo_time,
    "Date": echo_date,
    "Path": echo_path,
}

command_names = commands.keys()
