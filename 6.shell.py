#! usr/bin/python3
import os

# Changing the Current Working Directory
os.chdir('/home/')

# Decorating
columns, rows = os.get_terminal_size()
print("\n\n")
print("--- Welcome to Duong Dang Hung's shell ---\n\n".center(columns, " "))
print("*You are in the home directory, enter any command to execute*")

# Running the terminal
while True:
    command = input(">")
    if "cd" in command:
        try:
            os.chdir(command[3:])
        except FileNotFoundError:
            print("bash: cd: No such file or directory")
    elif command == 'exit':
        break
    else:
        os.system(command)

