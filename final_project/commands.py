from Rayanoos import tools
from utility import echo_command, echo_result

t = tools.SystemControls()


def mouse_move():
    echo_command("Mouse Move")
    x = int(input("X: "))
    y = int(input("Y: "))

    t.mouse_move_cursor(x, y)
    echo_result(f"Mouse moved to ({x},{y})")


commands = {
    "exit": exit,
    "Mouse Move": mouse_move
}
