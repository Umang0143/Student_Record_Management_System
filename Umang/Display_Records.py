import os

def displayrecords(path):
    if os.path.exists(path):
        with open(path, "r") as file:
            print(file.read())