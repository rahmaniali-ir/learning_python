
import os
import signal
from commands import commands
from utility import echo_bold, echo_command, echo_error

# welcome
os.system('cls')
print("\n@@ Final Project by Ali Rahmani")
print("@@ Enter 'help' to get list of supported commands")


# handle ctrl+c
def on_ctrl_c(signum, frame):
    echo_command("Exit")
    exit()


signal.signal(signal.SIGINT, on_ctrl_c)

# command loop
while True:
    echo_bold("\nEnter a command:")
    command = input(f"> ")
    command = command.replace(' ', '').lower()

    if command in commands.keys():
        echo_command(commands[command]['name'])
        commands[command]['func']()
    else:
        echo_error("Invalid command")

    print("\n-----------------------")
