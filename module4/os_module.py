import os
import shutil

"""
os module
"""


def list_dir():
    print(os.listdir())


def create_dir(_str):
    os.mkdir(_str)


def create_dirs(_str):
    os.makedirs(_str)


def remove_dir(_str):
    os.rmdir(_str)


def go_to_dir(_str):
    os.chdir(_str)


def remove_non_empty_dir(_str):
    shutil.rmtree(_str)


def execute_command(command):
    return os.system(command)


"""
Scenario
It goes without saying that operating systems allow you to search for files and directories. While studying this part of the course, you learned about the functions of the os module, which have everything you need to write a program that will search for directories in a given location.

To make your task easier, we have prepared a test directory structure for you:


Directory structure


Your program should meet the following requirements:

Write a function or method called find that takes two arguments called path and dir. The path argument should accept a relative or absolute path to a directory where the search should start, while the dir argument should be the name of a directory that you want to find in the given path. Your program should display the absolute paths if it finds a directory with the given name.
The directory search should be done recursively. This means that the search should also include all subdirectories in the given path.
Example input:

path="./tree", dir="python"

Example output:

.../tree/python
.../tree/cpp/other_courses/python
.../tree/c/other_courses/python
"""


def find_dir(path, dir):
    # Iterate through the contents of the directory
    for c_dir in os.listdir(path):
        # Construct the full path of the current entry
        full_path = os.path.join(path, c_dir)

        # Check if the current entry is a directory
        if os.path.isdir(full_path):
            # If the directory matches the target, print its absolute path
            if c_dir == dir:
                print(full_path)
            # Recursively search in the subdirectory
            find_dir(full_path, dir)


def main():
    list_dir()
    create_dir("temp")
    list_dir()
    remove_dir("temp")
    create_dirs("temp/temp1/temp2")
    list_dir()
    remove_non_empty_dir("temp")
    list_dir()
    # execute_command("dir")
    find_dir(r"C:\nvm4w", "npm")


if __name__ == "__main__":
    main()
