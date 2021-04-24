#! usr/bin/python3
import os


# Function to Get the current
# working directory
def current_path():
    print("Current working directory: ")
    print(os.getcwd())
    print()


# Changing the CWD
os.chdir('/home/bell')
while True:
    command = input(">")
    if "cd" in command:
        os.chdir(command[3:])
    elif command == 'exit':
        break
    else:
        os.system(command)

