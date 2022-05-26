
import os
import signal
from commands import commands
from colors import colors
from utility import echo_command

# welcome
os.system('cls')
print("\n@@ Final Project by Ali Rahmani")


# handle ctrl+c
def on_ctrl_c(signum, frame):
    echo_command("Exit")
    exit()


signal.signal(signal.SIGINT, on_ctrl_c)

# command loop
while True:
    print(f"\n{colors.BOLD}Enter a command:{colors.ENDC}")
    command = input(f"> ")
    command = command.replace(' ', '').lower()

    if command in commands.keys():
        echo_command(commands[command]['name'])
        commands[command]['func']()
    else:
        print("Invalid command!")

    print("\n-----------------------")
