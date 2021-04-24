#! usr/bin/python3
import os

# Changing the Current Working Directory
os.chdir(os.getenv("HOME"))

# Decorating
columns, rows = os.get_terminal_size()
print("\n\n")
print("--- Welcome to Duong Dang Hung's shell ---\n\n".center(columns, " "))

# Running the terminal
while True:
    command = input(">")
    if command.split()[0] == "cd":
        try:
            os.chdir(command[3:])
        except FileNotFoundError:
            print("bash: cd: No such file or directory")
    elif command == 'exit':
        break
    else:
        os.system(command)

