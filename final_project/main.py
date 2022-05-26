
from commands import commands

# removes the spaces & uppercase letters from the commands
newCommands = {}
for c in commands.keys():
    newCommands[c.replace(' ', '').lower()] = commands[c]
commands = newCommands
del newCommands

print("\nHey!\n")
while True:
    command = input("\nEnter a command: ")
    command = command.replace(' ', '').lower()

    if command in commands.keys():
        commands[command]()
    else:
        print("Invalid command!")
