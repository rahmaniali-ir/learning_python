import os
from Rayanoos import tools
from colors import colors
from utility import echo_result, get_confirmation
from files import get_file_name, get_folder_files, is_png

t = tools.SystemControls()


def exit_program():
    exit()


def mouse_move():
    x = int(input("X: "))
    y = int(input("Y: "))

    t.mouse_move_cursor(x, y)
    echo_result(f"Mouse moved to ({x},{y})")


def shutdown():
    confirmed = get_confirmation(
        "Are you sure you want to shut your system down?")

    if confirmed:
        t.force_shutdown()


def standby():
    confirmed = get_confirmation(
        "Are you sure you want to standby your system?")

    if confirmed:
        t.standby()


def reboot():
    confirmed = get_confirmation(
        "Are you sure you want to reboot your system?")

    if confirmed:
        t.reboot()


def kill_process():
    process = input("Enter the process name: ")
    "t".killprocess("process")

    echo_result(f"Closed '{ process }'")


def show_clipboard_content():
    echo_result("Showing notification")
    t.alert("Clipboard Content", t.clipboard_get(), 2000)
    echo_result("Notification closed")


def echo_time():
    echo_result(t.system_time())


def echo_date():
    echo_result(t.system_date())


def echo_username():
    echo_result(t.system_username())


def echo_path():
    echo_result(t.folder_windows())


def move_system_path():
    new_path = input("Source folder: ")
    os.chdir(new_path)

    cwd = os.getcwd()
    echo_result(f"Current directory: { cwd }")


def search_pic():
    source = input("Source folder: ")
    target = input("Target folder: ")

    files = list(filter(is_png, get_folder_files(source)))
    files_count = len(files)

    if files_count == 0:
        echo_result("No PNG files were found!")
        return

    echo_result(f"Found {files_count} PNG files")
    for file in files:
        print(file)

    print("\nConverting...")
    for file in files:
        file_name = get_file_name(file)
        print(f"Converting {file_name}.png")
        t.convert_image(file, f"{target}/{file_name}.jpg")

    echo_result(f"Converted the images and stored in {target}")


def show_help():
    for command in commands:
        print(
            f"{ commands[command]['name'] }: {colors.GRAY}{ commands[command]['comment'] }{colors.ENDC}")


commands = {
    "exit": {
        "name": "Exit",
        "func": exit_program,
        "comment": "Exit program"
    },
    "mousemove": {
        "name": "Mouse Move",
        "func": mouse_move,
        "comment": "Move mouse pointer to a given x, y"
    },
    "shutdown": {
        "name": "Shut Down",
        "func": shutdown,
        "comment": "Shut the system down"
    },
    "standby": {
        "name": "Standby",
        "func": standby,
        "comment": "Standby the system"
    },
    "reboot": {
        "name": "Reboot",
        "func": reboot,
        "comment": "Reboot the system"
    },
    "killprocess": {
        "name": "Kill process",
        "func": kill_process,
        "comment": "Kill a process by a given name"
    },
    "clipboard": {
        "name": "Clipboard",
        "func": show_clipboard_content,
        "comment": "Show a notification containing the clipboard content"
    },
    "time": {
        "name": "Time",
        "func": echo_time,
        "comment": "Show time"
    },
    "date": {
        "name": "Date",
        "func": echo_date,
        "comment": "Show date"
    },
    "path": {
        "name": "Path",
        "func": echo_path,
        "comment": "Get the current system path"
    },
    "movepath": {
        "name": "Move System Path",
        "func": move_system_path,
        "comment": "Move system path to the new path"
    },
    "searchpic": {
        "name": "Search Pic",
        "func": search_pic,
        "comment": "Convert png images of a given source into jpg and store to a given target"
    },
    "help": {
        "name": "Help",
        "func": show_help,
        "comment": "Show help"
    }
}
